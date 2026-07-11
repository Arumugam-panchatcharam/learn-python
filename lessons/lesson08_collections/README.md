# Lesson 08 — Collections

## Learning Goals

- Pick the right specialized container for the job
- Use `Counter` and `defaultdict` idiomatically
- Understand trade-offs of `deque` vs list

## Important Notes

- Read `theory.py` first for focused examples.
- Study `examples.py` from simple to professional.
- Attempt `exercises.py` before opening `solutions.py`.
- Keep code out of this README — notes live in [notes/lesson08.md](../../notes/lesson08.md).

## References

- [collections module](https://docs.python.org/3/library/collections.html)

## Pitfalls

- Using `defaultdict` when a plain dict with `.get()` is clearer
- Treating `namedtuple` like a full domain model
- Forgetting `Counter` arithmetic semantics
