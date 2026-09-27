"""Independent finite witnesses for a proposed static composition interface."""

import unittest

from finite_composition import Endpoint, EnumerationLimit, Relation, Wire, compose

BOOL = ("0", "1")
NOT = Relation(
    ports=(("input", BOOL), ("output", BOOL)),
    rows=(("0", "1"), ("1", "0")),
)
IDENTITY = Relation(
    ports=(("input", BOOL), ("output", BOOL)),
    rows=(("0", "0"), ("1", "1")),
)


class CompositionWitnessTests(unittest.TestCase):
    def test_two_negations_in_series_are_identity(self):
        result = compose(
            {"first": NOT, "second": NOT},
            (Wire(Endpoint("first", "output"), Endpoint("second", "input")),),
            (Endpoint("first", "input"), Endpoint("second", "output")),
        )
        self.assertEqual(set(result.relation.rows), {("0", "0"), ("1", "1")})
        self.assertEqual(result.compatible_assignments, 2)

    def test_same_components_in_feedback_have_two_joint_solutions(self):
        result = compose(
            {"first": NOT, "second": NOT},
            (
                Wire(Endpoint("first", "output"), Endpoint("second", "input")),
                Wire(Endpoint("second", "output"), Endpoint("first", "input")),
            ),
            (Endpoint("first", "input"), Endpoint("second", "input")),
        )
        self.assertEqual(set(result.relation.rows), {("0", "1"), ("1", "0")})
        self.assertEqual(result.compatible_assignments, 2)

    def test_self_negation_is_unsatisfiable_not_vacuously_valid(self):
        result = compose(
            {"one": NOT},
            (Wire(Endpoint("one", "output"), Endpoint("one", "input")),),
            (Endpoint("one", "input"),),
        )
        self.assertEqual(result.relation.rows, ())
        self.assertEqual(result.compatible_assignments, 0)
        self.assertEqual(result.status, "UNSAT")

    def test_self_identity_has_two_solutions(self):
        result = compose(
            {"one": IDENTITY},
            (Wire(Endpoint("one", "output"), Endpoint("one", "input")),),
            (Endpoint("one", "input"),),
        )
        self.assertEqual(set(result.relation.rows), {("0",), ("1",)})

    def test_incompatible_domains_are_rejected(self):
        alpha = Relation(ports=(("p", ("a", "b")),), rows=(("a",),))
        beta = Relation(ports=(("p", BOOL),), rows=(("0",),))
        with self.assertRaisesRegex(ValueError, "domain"):
            compose(
                {"a": alpha, "b": beta},
                (Wire(Endpoint("a", "p"), Endpoint("b", "p")),),
                (Endpoint("a", "p"),),
            )

    def test_missing_port_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown port"):
            compose({"one": NOT}, (), (Endpoint("one", "missing"),))

    def test_enumeration_limit_does_not_return_false_unsat(self):
        with self.assertRaises(EnumerationLimit):
            compose(
                {"first": NOT, "second": NOT},
                (),
                (Endpoint("first", "input"),),
                max_candidates=3,
            )

    def test_relation_rejects_rows_outside_declared_domain(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            Relation(ports=(("p", BOOL),), rows=(("x",),))

    def test_relation_rejects_mutable_structure(self):
        with self.assertRaisesRegex(TypeError, "tuples"):
            Relation(ports=[("p", BOOL)], rows=(("0",),))
        with self.assertRaisesRegex(TypeError, "tuples"):
            Relation(ports=(("p", BOOL),), rows=[["0"]])

    def test_adding_wire_cannot_create_a_visible_solution(self):
        nodes = {"first": NOT, "second": NOT}
        exposed = (Endpoint("first", "input"), Endpoint("second", "output"))
        unconstrained = compose(nodes, (), exposed)
        wired = compose(
            nodes,
            (Wire(Endpoint("first", "output"), Endpoint("second", "input")),),
            exposed,
        )
        self.assertTrue(set(wired.relation.rows) <= set(unconstrained.relation.rows))
        self.assertEqual(unconstrained.compatible_assignments, 4)
        self.assertEqual(wired.compatible_assignments, 2)

    def test_projection_removes_hidden_multiplicity_without_losing_count(self):
        result = compose(
            {"visible": NOT, "hidden": IDENTITY},
            (),
            (Endpoint("visible", "input"),),
        )
        self.assertEqual(set(result.relation.rows), {("0",), ("1",)})
        self.assertEqual(result.compatible_assignments, 4)

    def test_node_order_and_wire_orientation_do_not_change_static_relation(self):
        left = Endpoint("first", "output")
        right = Endpoint("second", "input")
        visible = (Endpoint("first", "input"), Endpoint("second", "output"))
        forward = compose({"first": NOT, "second": NOT}, (Wire(left, right),), visible)
        reordered = compose(
            {"second": NOT, "first": NOT}, (Wire(right, left),), visible
        )
        self.assertEqual(forward, reordered)

    def test_independent_bruteforce_oracle_for_two_negators(self):
        # Independent oracle: directly enumerate all four Boolean port values.
        expected = set()
        for first_input in BOOL:
            for first_output in BOOL:
                for second_input in BOOL:
                    for second_output in BOOL:
                        if (
                            first_output == ("1" if first_input == "0" else "0")
                            and second_output == ("1" if second_input == "0" else "0")
                            and first_output == second_input
                        ):
                            expected.add((first_input, second_output))
        result = compose(
            {"first": NOT, "second": NOT},
            (Wire(Endpoint("first", "output"), Endpoint("second", "input")),),
            (Endpoint("first", "input"), Endpoint("second", "output")),
        )
        self.assertEqual(set(result.relation.rows), expected)


if __name__ == "__main__":
    unittest.main()
