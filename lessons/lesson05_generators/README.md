# Lesson 05 — Generators

## Learning Goals

- Write generator functions with `yield`
- Delegate with `yield from`
- Choose between generators and lists for memory efficiency

## Important Notes

- Read `theory.py` first for focused examples.
- Study `examples.py` from simple to professional.
- Attempt `exercises.py` before opening `solutions.py`.
- Keep code out of this README — notes live in [notes/lesson05.md](../../notes/lesson05.md).

## References

- [Generator types](https://docs.python.org/3/glossary.html#term-generator)

## Pitfalls

- Trying to reuse a generator after exhaustion
- Mixing return values and yields in Python < 3.3 semantics confusion
- Building huge intermediate lists when a generator would work
