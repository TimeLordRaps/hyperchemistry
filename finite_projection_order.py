"""Finite witness: the order of mixed projections changes the result.

`finite_composition.compose` uses only existential projection, and existential
projections commute with each other. This module adds the other quantifier, so
that the same two projections applied to the same relation in a different order
can be compared exactly.

Scope. Finite domains, no time index, no physical unit, no claim that a
hyperphysics operation is a finite relation. A limit procedure is *not* modelled
here: limits need infinite domains, which lie outside this model's envelope.
What the module exhibits is the shape of the failure that makes an exchange of
limits fail -- an exchange of quantifiers -- in a setting small enough to
enumerate.
"""

from __future__ import annotations

from itertools import permutations
from typing import Mapping

from finite_composition import Relation

EXISTS = "exists"
FORALL = "forall"

Prefix = tuple[tuple[str, str], ...]


def holds(relation: Relation, prefix: Prefix) -> bool:
    """Truth of the quantified statement `prefix relation`, outermost first.

    Every port of `relation` must be quantified exactly once. `("x", FORALL),
    ("y", EXISTS)` reads: for every value of x there is a value of y such that
    `(x, y)` is a row.
    """
    names = [name for name, _ in relation.ports]
    domains = dict(relation.ports)
    quantified = [name for name, _ in prefix]
    if sorted(quantified) != sorted(names):
        raise ValueError(
            f"prefix must quantify every port exactly once: ports {names}, prefix {quantified}"
        )
    for _, quantifier in prefix:
        if quantifier not in (EXISTS, FORALL):
            raise ValueError(f"unknown quantifier: {quantifier!r}")
    rows = set(relation.rows)

    def go(index: int, assignment: dict[str, str]) -> bool:
        if index == len(prefix):
            return tuple(assignment[name] for name in names) in rows
        name, quantifier = prefix[index]
        outcomes = (go(index + 1, {**assignment, name: value}) for value in domains[name])
        return any(outcomes) if quantifier == EXISTS else all(outcomes)

    return go(0, {})


def order_results(
    relation: Relation, quantifiers: Mapping[str, str]
) -> dict[tuple[str, ...], bool]:
    """Evaluate every ordering of the same port-to-quantifier assignment."""
    return {
        order: holds(relation, tuple((name, quantifiers[name]) for name in order))
        for order in permutations(quantifiers)
    }
