# Lesson 01 — Advanced Functions

## Learning Goals

- Use `*args` and `**kwargs` intentionally
- Write and understand closures
- Pass functions as values and return functions from functions
- Read positional-only and keyword-only parameter syntax

## Important Notes

- Read `theory.py` first for focused examples.
- Study `examples.py` from simple to professional.
- Attempt `exercises.py` before opening `solutions.py`.
- Keep code out of this README — notes live in [notes/lesson01.md](../../notes/lesson01.md).

## References

- [PEP 3102 — Keyword-only arguments](https://peps.python.org/pep-3102/)
- [PEP 570 — Positional-only parameters](https://peps.python.org/pep-0570/)
- [functools docs](https://docs.python.org/3/library/functools.html)

## Pitfalls

- Using `*args` when explicit parameters would be clearer
- Mutable default arguments in nested functions
- Confusing closure late-binding in loops
