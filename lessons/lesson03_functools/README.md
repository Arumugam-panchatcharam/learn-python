# Lesson 03 — Functools

## Learning Goals

- Use `partial` to specialize callables
- Apply caching appropriately with `lru_cache`
- Understand single-dispatch generic functions

## Important Notes

- Read `theory.py` first for focused examples.
- Study `examples.py` from simple to professional.
- Attempt `exercises.py` before opening `solutions.py`.
- Keep code out of this README — notes live in [notes/lesson03.md](../../notes/lesson03.md).

## References

- [functools module](https://docs.python.org/3/library/functools.html)

## Pitfalls

- Caching functions with unhashable or mutable arguments
- Using `lru_cache` on methods without understanding instance identity
- Over-caching cheap functions
