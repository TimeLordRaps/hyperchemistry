# hyperchemistry

Status, 2026-09-27: **[FRAME] first public research candidate**. This is an
executable account of a finite composition question, not a grounded field layer
or a versioned release.

The author's 2026-09-20 [field-stack declaration](https://github.com/TimeLordRaps/hyperphysics/blob/08ef93f6134548fdfd14775e25684093f4e5a875/FIELD_STACK.md)
names hyperchemistry as **the operation of operations within hyperphysics**.
Hyperphysics' own ground (graduation criterion 5, GC-5) and transport soundness
(graduation criterion 4, GC-4) remain open. Its published electrical laws are a
citation and transport surface, not a supply of grounded hyperphysical
operations.

This candidate asks a narrower, refutable question: **when the same operations
are wired differently, can their composite admissible states differ?** The
finite static model in [COMPOSITION_CONTRACT.md](COMPOSITION_CONTRACT.md) says yes.
Two Boolean negations in series realize identity; the same two in a closed
feedback wiring have two joint solutions; a negation wired to itself has none.
Those are exact results about finite relations and wiring, with no clock,
physical unit, dynamics, or biological criterion. They do not derive this field
from hyperphysics. The model is an interface candidate to be accepted, revised,
or rejected once hyperphysics defines its operations.

[`finite_composition.py`](finite_composition.py) is an executable witness. It checks port domains,
joint satisfiability, exposed assignments, and the distinction between zero
solutions and an unfinished enumeration. Run the demonstration and checks with:

```text
python -m examples.negation_networks
python -m unittest discover -s tests -v
```

Next dependency: specify a hyperphysics operation carrier, admissible relation,
type/interface rule and identity/equivalence criterion, then prove or refute a
map into this finite model for the relevant bounded case. A hyperbiology layer
can consume a hyperchemistry composite only after that boundary and its
observation/whole criterion are separately justified.
