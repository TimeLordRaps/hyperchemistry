# hyperchemistry

Status, 2026-09-27: **[FRAME] first public research candidate**. This is an
executable account of a finite composition question, not a grounded field layer
or a versioned release.

The author's 2026-09-20 [field-stack declaration](https://github.com/TimeLordRaps/hyperphysics/blob/08ef93f6134548fdfd14775e25684093f4e5a875/FIELD_STACK.md)
names hyperchemistry as **the operation of operations within hyperphysics**.
That phrase is a research direction, not a derivation. Hyperphysics' own ground
(graduation criterion 5, GC-5) and transport soundness (graduation criterion 4,
GC-4) remain open. GC-5 asks for hyperphysics' own ground from which circuit
theory would follow; it is a distinct physical-specialization obligation, not
the sole source of structure, mechanics, or dynamics. Published electrical laws
are a citation and transport surface, not grounded operations.

This candidate asks a narrower, refutable question: **when the same operations
are wired differently, can their composite admissible states differ?** The
finite static model in [COMPOSITION_CONTRACT.md](COMPOSITION_CONTRACT.md) says yes.
Two Boolean negations in series realize identity; the same two in a closed
feedback wiring have two joint solutions; a negation wired to itself has none.
Those are exact results about finite relations and wiring, with no clock,
physical unit, dynamics, or biological criterion. They do not derive this field
from any other field. The model is an interface candidate to be accepted,
revised, or rejected against separately justified source operations.

[`finite_composition.py`](finite_composition.py) is an executable witness. It checks port domains,
joint satisfiability, exposed assignments, and the distinction between zero
solutions and an unfinished enumeration. Run the demonstration and checks with:

```text
python -m examples.negation_networks
python -m examples.projection_order
python -m unittest discover -s tests -v
```

The current work-in-progress handoff has separate obligations: Hyperstructure
binds component identity and kinds; Hypermechanics supplies guarded realized
operations; Hyperdynamics tests paths and coupled variation when such claims
are made; Hyperchemistry composes operations with explicit wiring and
interfaces. A local finite witness checks one chain and rejects invented steps
and rows, but these field contracts are not yet published here or natively
derived. Hyperphysics must separately add physical quantities, laws, units,
balances, and its own GC-5 ground. Hyperbiology needs its own observation and
whole criterion before consuming any composite.

[`finite_projection_order.py`](finite_projection_order.py) adds the other quantifier so
the order of two projections can be compared exactly: over all relations on `B x B`, the
two where the order is observable are the identity and the negation this contract
already uses (see "Order of projections" in the contract). It models the shape of an
exchange of limits, not limits themselves.
