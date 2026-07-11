# Lesson 09 — Context Managers

## Learning Goals

- Use `with` for resource management
- Implement context managers as classes and with `contextlib`
- Compose context managers safely

## Important Notes

- Read `theory.py` first for focused examples.
- Study `examples.py` from simple to professional.
- Attempt `exercises.py` before opening `solutions.py`.
- Keep code out of this README — notes live in [notes/lesson09.md](../../notes/lesson09.md).

## References

- [contextlib module](https://docs.python.org/3/library/contextlib.html)

## Pitfalls

- Swallowing exceptions in `__exit__` incorrectly
- Forgetting cleanup when an exception occurs
- Reinventing `contextlib.closing` or `suppress`
