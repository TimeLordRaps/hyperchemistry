"""Show that the same two projections give different results in different orders."""

from finite_composition import Relation
from finite_projection_order import EXISTS, FORALL, order_results

BOOL = ("0", "1")
CASES = {
    "identity": Relation(ports=(("x", BOOL), ("y", BOOL)), rows=(("0", "0"), ("1", "1"))),
    "negation": Relation(ports=(("x", BOOL), ("y", BOOL)), rows=(("0", "1"), ("1", "0"))),
    "constant y=1 (control)": Relation(
        ports=(("x", BOOL), ("y", BOOL)), rows=(("0", "1"), ("1", "1"))
    ),
}


def main() -> None:
    for name, relation in CASES.items():
        results = order_results(relation, {"x": FORALL, "y": EXISTS})
        pretty = {" ".join(order): value for order, value in results.items()}
        verdict = "order matters" if len(set(results.values())) > 1 else "order does not matter"
        print(f"{name}: {pretty}; {verdict}")


if __name__ == "__main__":
    main()
