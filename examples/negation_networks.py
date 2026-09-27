"""Show how the same finite operations differ under different wiring."""

from finite_composition import Endpoint, Relation, Wire, compose

BOOL = ("0", "1")
NEGATION = Relation(
    ports=(("input", BOOL), ("output", BOOL)),
    rows=(("0", "1"), ("1", "0")),
)


def main() -> None:
    first_in = Endpoint("first", "input")
    first_out = Endpoint("first", "output")
    second_in = Endpoint("second", "input")
    second_out = Endpoint("second", "output")
    nodes = {"first": NEGATION, "second": NEGATION}

    serial = compose(nodes, (Wire(first_out, second_in),), (first_in, second_out))
    loop = compose(
        nodes,
        (Wire(first_out, second_in), Wire(second_out, first_in)),
        (first_in, second_in),
    )
    impossible = compose(
        {"first": NEGATION},
        (Wire(first_out, first_in),),
        (first_in,),
    )

    for name, result in (
        ("serial", serial),
        ("closed loop", loop),
        ("self negation", impossible),
    ):
        print(
            f"{name}: {result.status}; rows={result.relation.rows}; "
            f"joint assignments={result.compatible_assignments}"
        )


if __name__ == "__main__":
    main()
