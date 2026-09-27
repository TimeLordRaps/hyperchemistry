"""Finite, static relation composition witness; not a hyperphysics ground.

The model has no time index, physical units, causal direction, or claim that a
hyperphysics operation is already a finite relation. It is a conditional model
of one possible meaning of "operation of operations."
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import prod
from typing import Mapping


@dataclass(frozen=True)
class Relation:
    """A finite set of admissible assignments to named, typed ports."""

    ports: tuple[tuple[str, tuple[str, ...]], ...]
    rows: tuple[tuple[str, ...], ...]

    def __post_init__(self) -> None:
        if (
            type(self.ports) is not tuple
            or type(self.rows) is not tuple
            or any(type(port) is not tuple for port in self.ports)
            or any(type(row) is not tuple for row in self.rows)
        ):
            raise TypeError("relation ports and rows must be tuples throughout")
        names = [name for name, _ in self.ports]
        if not names or len(set(names)) != len(names):
            raise ValueError("relation needs distinct named ports")
        for name, domain in self.ports:
            if not isinstance(name, str) or not name:
                raise ValueError("port names must be nonempty strings")
            if (
                not isinstance(domain, tuple)
                or not domain
                or any(not isinstance(value, str) or not value for value in domain)
                or len(set(domain)) != len(domain)
            ):
                raise ValueError(
                    "each port needs a nonempty finite domain of distinct strings"
                )
        if len(set(self.rows)) != len(self.rows):
            raise ValueError("relation rows must be distinct")
        for row in self.rows:
            if not isinstance(row, tuple) or len(row) != len(self.ports):
                raise ValueError("each row must assign every port once")
            if any(value not in domain for value, (_, domain) in zip(row, self.ports)):
                raise ValueError("relation row contains a value outside a port domain")


@dataclass(frozen=True)
class Endpoint:
    node: str
    port: str


@dataclass(frozen=True)
class Wire:
    left: Endpoint
    right: Endpoint


@dataclass(frozen=True)
class CompositionResult:
    relation: Relation
    compatible_assignments: int

    @property
    def status(self) -> str:
        """Finite satisfiability only; never a scientific or VSTD PASS."""
        return "SAT" if self.compatible_assignments else "UNSAT"


class EnumerationLimit(RuntimeError):
    """The requested exact enumeration was not completed."""


def compose(
    nodes: Mapping[str, Relation],
    wires: tuple[Wire, ...],
    exposed: tuple[Endpoint, ...],
    *,
    max_candidates: int = 1_000_000,
) -> CompositionResult:
    """Conjoin node relations and wire equalities, then project exposed ports.

    Every node chooses one admissible row. A wire equates its endpoints. The
    resulting relation contains distinct exposed assignments from compatible
    choices. `compatible_assignments` counts the full assignments before
    projection, retaining whether hidden structure has multiple solutions.
    """
    if not nodes or not exposed:
        raise ValueError("composition needs at least one node and exposed port")
    if type(max_candidates) is not int or max_candidates < 1:
        raise ValueError("max_candidates must be a positive integer")
    if len(set(exposed)) != len(exposed):
        raise ValueError("exposed endpoints must be distinct")
    for name, relation in nodes.items():
        if not isinstance(name, str) or not name or "." in name:
            raise ValueError("node names must be nonempty and contain no dot")
        if not isinstance(relation, Relation):
            raise TypeError("every node must contain a Relation")

    port_domains = {
        Endpoint(node_name, port_name): domain
        for node_name, relation in nodes.items()
        for port_name, domain in relation.ports
    }

    for endpoint in (*exposed, *(e for wire in wires for e in (wire.left, wire.right))):
        if endpoint not in port_domains:
            raise ValueError(f"unknown port: {endpoint}")
    for wire in wires:
        if port_domains[wire.left] != port_domains[wire.right]:
            raise ValueError(f"wire endpoints have different domains: {wire}")

    candidate_count = prod(len(relation.rows) for relation in nodes.values())
    if candidate_count > max_candidates:
        raise EnumerationLimit(
            f"exact enumeration requires {candidate_count} candidates; "
            f"limit is {max_candidates}"
        )

    node_items = tuple(nodes.items())
    visible_rows: set[tuple[str, ...]] = set()
    compatible = 0
    for chosen_rows in product(*(relation.rows for _, relation in node_items)):
        assignment = {
            Endpoint(node_name, port_name): value
            for (node_name, relation), row in zip(node_items, chosen_rows)
            for (port_name, _), value in zip(relation.ports, row)
        }
        if all(assignment[wire.left] == assignment[wire.right] for wire in wires):
            compatible += 1
            visible_rows.add(tuple(assignment[endpoint] for endpoint in exposed))

    visible = Relation(
        ports=tuple(
            (f"{endpoint.node}.{endpoint.port}", port_domains[endpoint])
            for endpoint in exposed
        ),
        rows=tuple(sorted(visible_rows)),
    )
    return CompositionResult(visible, compatible)
