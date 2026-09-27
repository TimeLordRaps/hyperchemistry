# Technical debt and open dependencies

| ID | Status | Location and evidence | Consequence | Revisit gate |
|---|---|---|---|---|
| HC-001 | OPEN | `COMPOSITION_CONTRACT.md`: hyperphysics graduation criterion 5 (GC-5) is unwritten; the relation carrier is conditional | No grounded hyperchemistry layer or derivation claim | Revisit when hyperphysics defines its operation carrier |
| HC-002 | OPEN | `finite_composition.py`: exact Cartesian enumeration is bounded but exponential | Large systems stop with `EnumerationLimit` | Optimize only when a real bounded application requires it, preserving the same relation semantics and negative controls |
| HC-003 | OPEN | `COMPOSITION_CONTRACT.md`: no source-to-relation map, physical units, or conservation argument | No physical or cross-field soundness claim | Revisit with a specific hyperphysics operation and application envelope |

Local check on 2026-09-27: thirteen `unittest` cases pass under the current Python
environment after an initial absent-module RED and a corrected port-name error.
No package build, alternate platform, or hyperphysics integration check has run.
