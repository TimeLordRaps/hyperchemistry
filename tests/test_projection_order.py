"""Finite witnesses that the order of mixed projections matters.

Existential projection is all `compose` uses. Once a universal projection is
allowed, two operations applied to the same relation in a different order give
different results. Every claim below is checked by exhaustive enumeration over
finite domains, not sampled.
"""

import unittest
from itertools import combinations, product

from finite_composition import Relation
from finite_projection_order import EXISTS, FORALL, holds, order_results

BOOL = ("0", "1")
PAIRS = tuple(product(BOOL, BOOL))
IDENTITY = Relation(ports=(("input", BOOL), ("output", BOOL)), rows=(("0", "0"), ("1", "1")))
NOT = Relation(ports=(("input", BOOL), ("output", BOOL)), rows=(("0", "1"), ("1", "0")))


def relation(rows):
    return Relation(ports=(("x", BOOL), ("y", BOOL)), rows=tuple(sorted(rows)))


def all_relations_on_bool_squared():
    for size in range(len(PAIRS) + 1):
        for rows in combinations(PAIRS, size):
            yield relation(rows)


class OrderOfProjectionTests(unittest.TestCase):
    def test_identity_for_all_then_exists_differs_from_exists_then_for_all(self):
        forall_exists = holds(IDENTITY, (("input", FORALL), ("output", EXISTS)))
        exists_forall = holds(IDENTITY, (("output", EXISTS), ("input", FORALL)))
        self.assertTrue(forall_exists)
        self.assertFalse(exists_forall)

    def test_negation_behaves_the_same_way(self):
        self.assertTrue(holds(NOT, (("input", FORALL), ("output", EXISTS))))
        self.assertFalse(holds(NOT, (("output", EXISTS), ("input", FORALL))))

    def test_exists_exists_and_forall_forall_commute_on_every_relation(self):
        for rel in all_relations_on_bool_squared():
            for q in (EXISTS, FORALL):
                a = holds(rel, (("x", q), ("y", q)))
                b = holds(rel, (("y", q), ("x", q)))
                self.assertEqual(a, b, (rel.rows, q))

    def test_exists_for_all_always_implies_for_all_exists(self):
        for rel in all_relations_on_bool_squared():
            if holds(rel, (("y", EXISTS), ("x", FORALL))):
                self.assertTrue(holds(rel, (("x", FORALL), ("y", EXISTS))), rel.rows)

    def test_the_converse_fails_for_exactly_the_negation_and_identity_relations(self):
        witnesses = {
            rel.rows
            for rel in all_relations_on_bool_squared()
            if holds(rel, (("x", FORALL), ("y", EXISTS)))
            and not holds(rel, (("y", EXISTS), ("x", FORALL)))
        }
        self.assertEqual(witnesses, {IDENTITY.rows, NOT.rows})

    def test_a_relation_with_a_constant_column_commutes_as_a_negative_control(self):
        constant = relation({("0", "1"), ("1", "1")})
        self.assertTrue(holds(constant, (("x", FORALL), ("y", EXISTS))))
        self.assertTrue(holds(constant, (("y", EXISTS), ("x", FORALL))))

    def test_empty_and_full_relations_agree_in_both_orders(self):
        for rows, expected in ((set(), False), (set(PAIRS), True)):
            rel = relation(rows)
            self.assertEqual(holds(rel, (("x", FORALL), ("y", EXISTS))), expected)
            self.assertEqual(holds(rel, (("y", EXISTS), ("x", FORALL))), expected)

    def test_the_effect_is_not_an_artifact_of_two_element_domains(self):
        abc = ("a", "b", "c")
        differ = Relation(
            ports=(("x", abc), ("y", abc)),
            rows=tuple((p, q) for p in abc for q in abc if p != q),
        )
        self.assertTrue(holds(differ, (("x", FORALL), ("y", EXISTS))))
        self.assertFalse(holds(differ, (("y", EXISTS), ("x", FORALL))))

    def test_order_results_lists_every_order_of_the_same_quantifier_assignment(self):
        results = order_results(IDENTITY, {"input": FORALL, "output": EXISTS})
        self.assertEqual(
            results,
            {("input", "output"): True, ("output", "input"): False},
        )

    def test_malformed_prefixes_are_rejected(self):
        with self.assertRaises(ValueError):
            holds(IDENTITY, (("input", FORALL),))  # a port left unquantified
        with self.assertRaises(ValueError):
            holds(IDENTITY, (("input", FORALL), ("input", EXISTS)))
        with self.assertRaises(ValueError):
            holds(IDENTITY, (("input", FORALL), ("nowhere", EXISTS)))
        with self.assertRaises(ValueError):
            holds(IDENTITY, (("input", "sometimes"), ("output", EXISTS)))


if __name__ == "__main__":
    unittest.main()
