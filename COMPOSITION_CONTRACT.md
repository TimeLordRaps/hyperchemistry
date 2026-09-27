# A conditional composition law for operations

Status: **[FRAME] mathematical model and executable finite witness**, not a
hyperphysics derivation. `[FORM]` below denotes a claim proved within the
stated finite-set model only. `[OPEN]` denotes an unsupplied field interface or
proof obligation. `[HYPER]` would require an explicit cross-level map; none is
claimed here. These are epistemic classifications, not certification.

## Ancestry and scope

The governing author declaration is quoted in
[hyperphysics' field stack](https://github.com/TimeLordRaps/hyperphysics/blob/08ef93f6134548fdfd14775e25684093f4e5a875/FIELD_STACK.md):
hyperchemistry is “the operation of operations within hyperphysics.” The
[published `electrical.hm`](https://github.com/TimeLordRaps/hyperphysics/blob/08ef93f6134548fdfd14775e25684093f4e5a875/electrical.hm)
states that its ground, graduation criterion 5 (GC-5), is unwritten. The seven
electrical laws and `SERIES_RLC_CONSTITUENTS` describe a
physical citation and dependency surface. Their composition of law forms is a
useful case to investigate later, but a law name or equation string is not yet a
hyperphysical operation. No equation is silently cast to an operation here.

The phrase *operation of operations* is retained as the field's subject. The
finite relations below supply one candidate mechanism, not its definition by
fiat. Hypermechanics' transition relations and hyperdynamics' trajectories are
not imported. Feedback here is a simultaneous constraint, not time evolution.

## Finite model

Let `I` be a finite set of component indices and `P_i` a finite set of port
names for component `i` in `I`. A port `p` in `P_i` has a finite, nonempty value
domain `D_(i,p)`. Each component operation is represented by a relation
`R_i` contained in the Cartesian product of its port domains: the set of
admissible assignments to its ports. A relation may be empty. These values are symbols without physical
units; the Boolean examples use `0` and `1`, dimensionless tokens, not volts or
seconds. Port direction, causation and scheduling are deliberately absent.

A wiring `W` is a finite set of pairs of ports whose domains are **exactly
equal**. Each pair demands equality of values. An exposed ordered port list
`E = (e_1, ..., e_m)` names the interface visible to a caller. The composite
relation is

```text
C_W,E(R_i : i in I) = {
  (a[e_1], ..., a[e_m]) :
  for every i, a restricted to P_i belongs to R_i,
  and for every (u,v) in W, a[u] = a[v]
}.
```

Here `a` is a joint assignment of values to every qualified component port;
`restricted to` means selecting that component's ports. Exposing `E` is
existential projection of hidden ports. `compatible_assignments` counts full
joint assignments before projection; duplicate visible tuples are collapsed in
the resulting relation. All sets and products are finite. The executable model
enumerates candidates up to an explicit bound; exceeding it raises
`EnumerationLimit`, not a false `UNSAT` (unsatisfiable) or a scientific
`UNKNOWN` verdict.

**[FORM, within this model]** Composition is invariant under permuting the
order in which component predicates and wire equalities are conjoined: logical
conjunction is associative and commutative. This does **not** permit hiding an
interface port before a later wiring needs it. Existential projection generally
cannot be moved across a constraint mentioning the hidden variable. Thus a
valid decomposition carries every future connection as an exposed interface.

**[FORM, within this model]** Domain mismatch is rejected, an empty composite
has zero admissible joint assignments, and a satisfiable composite may have more
joint assignments than distinct exposed rows. These are consequences of the
set construction, not claims about nature.

## Witness and counterexamples

Let `B = {0, 1}` and `N = {(0,1), (1,0)}` contained in `B × B` be a Boolean
negation relation with `input` and `output` ports. The two ports have no
physical unit. With two copies `N_1` and `N_2`:

| Wiring | Exposed ports | Composite rows | Consequence |
|---|---|---|---|
| `N1.output = N2.input` | `N1.input`, `N2.output` | `(0,0)`, `(1,1)` | serial double negation is identity |
| the above plus `N2.output = N1.input` | `N1.input`, `N2.input` | `(0,1)`, `(1,0)` | same components, two compatible joint states |
| one negation with `output = input` | its `input` | none | no fixed assignment, explicitly `UNSAT` |

These results falsify the rule “component inventory alone determines the
composite.” They do not prove that all wiring creates a novel operation or that
these constraints represent physical feedback. The identity self-loop is a
nearby negative control: it has two assignments, so a cycle alone does not
imply impossibility.

## Exact hyperphysics case to which the model must answer

The source repo's
[electrical-law definitions](https://github.com/TimeLordRaps/hyperphysics/blob/08ef93f6134548fdfd14775e25684093f4e5a875/src/hyperphysics/electrical.py)
declare that the series resistor–inductor–capacitor (RLC) equation composes
Ohm's resistor law, the Faraday–Lenz inductor law, the capacitor law, and
Kirchhoff's loop voltage law. This is a **documented source case**, not a
hyperphysics ground or a proof that the finite model applies to differential
equations. For an idealized lumped circuit with constant parameters, the
simultaneous constraints are:

```text
V_R = R I                    resistor
V_L = L dI/dt                inductor
V_C = Q/C                   capacitor
V_applied = V_R + V_L + V_C loop balance
I = dQ/dt                   shared state relation
```

`Q` is electric charge in coulombs; `I` is current in amperes; `t` is physical
time in seconds; `R` is resistance in ohms; `L` is inductance in henries; `C`
is capacitance in farads; and each `V` is a voltage in volts. Substitution
under those stated assumptions yields
`L d²Q/dt² + R dQ/dt + Q/C = V_applied`, with every term in volts. The
composition identifies shared quantities and conjoins constraints. It must
also inherit each constituent law's validity envelope and failure modes;
`SERIES_RLC_CONSTITUENTS` names those four constituents in the source. A
finite symbolic port-domain match alone does not perform that inheritance,
derive the differential equation, check units, or validate a transport.

This case supplies a concrete falsification target for future integration:
if a proposed hyperchemistry composition map loses the shared state relation,
permits adding unlike dimensions, or drops a constituent failure mode, it does
not preserve even the available hyperphysics citation surface. Passing that
case would still leave GC-5 and the field-level operation map open.

## Binding obligations and promotion gates

**[OPEN] Hyperphysics source.** GC-5 must define the operation carrier, its
static features, admissibility and identity/equivalence. Identify an exact
source version and prove what, if anything, corresponds to a port relation.
The current electrical-law strings cannot fill that slot by naming them so.

**[OPEN] Preservation.** If a map from hyperphysics operations to relations is
proposed, state which compositions and distinctions it preserves and which it
forgets. A finite truncation of an infinite domain needs an explicit envelope;
outside it the field claim is `UNKNOWN` or `OUT_OF_BOUNDS` as its contract
requires, never a theorem extrapolated from finite enumeration.

**[OPEN] Physical application.** Supply a measurement/units map, constitutive
law applicability, boundary exchanges and applicable mass, momentum, energy,
charge and species balances before interpreting a composite physically. Domain
equality of symbolic tokens is insufficient for dimensional soundness.

**[OPEN] Hyperbiology handoff.** A composite relation is not a comprehended
whole. Hyperbiology must independently specify the observer, quotient/whole
criterion and what information is retained or lost. The finite witness in
`hyperbiology/research/COMPREHENSION_WITNESS.md` is related research, not proof
that this interface binds to that field.

**[OPEN] Verifier Standard (VSTD) claims.** A test result about this finite
model is not a VSTD grounded certificate or evidence that graduation criterion
4 (GC-4), transport soundness, is resolved. Any later verification receipt needs the exact claim,
artifact digest, source coordinate, translation, mechanism, assumptions,
exclusions, invalidators and a supported `PASS`/`FAIL`/`UNKNOWN` judgment.
