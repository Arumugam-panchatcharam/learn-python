# Lesson 04 — Iterators

## Learning Goals

- Distinguish iterables from iterators
- Implement the iterator protocol
- Know when to use iterators vs sequences

## Important Notes

- Read `theory.py` first for focused examples.
- Study `examples.py` from simple to professional.
- Attempt `exercises.py` before opening `solutions.py`.
- Keep code out of this README — notes live in [notes/lesson04.md](../../notes/lesson04.md).

## References

- [Iterator types](https://docs.python.org/3/library/stdtypes.html#iterator-types)

## Pitfalls

- Implementing only `__iter__` without `__next__`
- Reusing exhausted iterators unexpectedly
- Confusing iterator classes with generator functions
