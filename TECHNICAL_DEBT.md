# Technical debt and open dependencies

| ID | Status | Location and evidence | Consequence | Revisit gate |
|---|---|---|---|---|
| HC-001 | OPEN | `COMPOSITION_CONTRACT.md`: hyperphysics graduation criterion 5 (GC-5) is unwritten; the relation carrier is conditional | No grounded hyperchemistry layer or derivation claim | Revisit when hyperphysics defines its operation carrier |
| HC-002 | OPEN | `finite_composition.py`: exact Cartesian enumeration is bounded but exponential | Large systems stop with `EnumerationLimit` | Optimize only when a real bounded application requires it, preserving the same relation semantics and negative controls |
| HC-003 | OPEN | `COMPOSITION_CONTRACT.md`: no source-to-relation map, physical units, or conservation argument | No physical or cross-field soundness claim | Revisit with a specific hyperphysics operation and application envelope |
| HC-004 | OPEN | `COMPOSITION_CONTRACT.md`, "Order of projections": no typed map from a limit word to a quantifier prefix over a finite truncation | Order of limits and order of projections are related by analogy of shape only | Revisit with an explicit envelope and a hyperphysics operation |
| HC-005 | OPEN | The contract cites `hyperphysics.limits` at a commit on the unmerged branch `claude/order-of-limits` | The citation resolves only while that commit stays reachable | Re-cite the merge commit once the hyperphysics branch is merged |

Local check on 2026-09-27: thirteen `unittest` cases pass under the current Python
environment after an initial absent-module RED and a corrected port-name error.
No package build, alternate platform, or hyperphysics integration check has run.

Local check on 2026-10-03: twenty-three `unittest` cases pass on Python 3.11 (thirteen
earlier plus ten for `finite_projection_order.py`) after an initial absent-module RED.
Four mutants of the new module (swapped quantifiers, ignored order, always-existential,
skipped port-coverage check) each failed at least one test. The CI matrix (3.12, 3.13)
and any hyperphysics integration check have not run.
