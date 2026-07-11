# Lesson 07 — Dataclasses

## Learning Goals

- Replace boilerplate classes with `@dataclass`
- Choose options like `frozen=True` and `slots=True`
- Compare dataclasses with namedtuple and Pydantic models

## Important Notes

- Read `theory.py` first for focused examples.
- Study `examples.py` from simple to professional.
- Attempt `exercises.py` before opening `solutions.py`.
- Keep code out of this README — notes live in [notes/lesson07.md](../../notes/lesson07.md).

## References

- [PEP 557 — Dataclasses](https://peps.python.org/pep-0557/)
- [dataclasses module](https://docs.python.org/3/library/dataclasses.html)

## Pitfalls

- Using mutable defaults without `field(default_factory=...)`
- Assuming dataclasses validate data automatically
- Choosing dataclasses when a TypedDict or Protocol is enough
