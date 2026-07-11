# Lesson 02 — Decorators

## Learning Goals

- Explain what a decorator does at runtime
- Write decorators with and without arguments
- Preserve function metadata with `functools.wraps`

## Important Notes

- Read `theory.py` first for focused examples.
- Study `examples.py` from simple to professional.
- Attempt `exercises.py` before opening `solutions.py`.
- Keep code out of this README — notes live in [notes/lesson02.md](../../notes/lesson02.md).

## References

- [Primer on Python decorators](https://realpython.com/primer-on-python-decorators/)
- [functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)

## Pitfalls

- Forgetting to use `@wraps`
- Decorators that hide required arguments
- Overusing decorators for simple one-off behavior
