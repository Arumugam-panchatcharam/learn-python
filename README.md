# Learning Python

A structured, professional roadmap for learning modern Python — from fundamentals through production-quality patterns.

## How to Use This Repo

1. Start with [Lesson 01 — Naming](module-01-modern-python/lesson-01/lesson-01.md).
2. Follow the [lesson structure](lesson-structure.md) used in every lesson.
3. Work through the [curriculum](#curriculum) in order, or jump to a [module folder](#module-folders) directly.

Each lesson includes theory, examples, common mistakes, a mini challenge, and a code review.

---

## Curriculum

### Module 1 — Modern Python

[module-01-modern-python/](module-01-modern-python/README.md)

- [01 — Naming](module-01-modern-python/lesson-01/lesson-01.md)
- [02 — Imports](module-01-modern-python/lesson-02/lesson-02.md)
- [03 — Modules](module-01-modern-python/lesson-03/lesson-03.md)
- [04 — Packages](module-01-modern-python/lesson-04/lesson-04.md)
- [05 — Virtual Environments](module-01-modern-python/lesson-05/lesson-05.md)
- [06 — PEP 8](module-01-modern-python/lesson-06/lesson-06.md)
- [07 — Type Hints](module-01-modern-python/lesson-07/lesson-07.md)
- [08 — Docstrings](module-01-modern-python/lesson-08/lesson-08.md)
- [09 — Context Managers](module-01-modern-python/lesson-09/lesson-09.md)
- [10 — Enumerations](module-01-modern-python/lesson-10/lesson-10.md)

### Module 2 — Functions (Advanced)

[module-02-functions-advanced/](module-02-functions-advanced/README.md)

- `*args` and `**kwargs`
- Keyword-only arguments (`def foo(a, *, debug=False)`)
- Positional-only arguments (`def foo(a, /)`)
- Closures and nested functions
- First-class functions
- Decorators
- Callable objects
- Lambda, partial functions, and higher-order functions

### Module 3 — Functional Python

[module-03-functional-python/](module-03-functional-python/README.md)

- `map`, `filter`, `reduce`
- `functools` (`partial`, `wraps`, `cache`, `lru_cache`, `singledispatch`)
- `operator` module
- `itertools`

### Module 4 — Collections

[module-04-collections/](module-04-collections/README.md)

- `collections` module
- `defaultdict`, `Counter`, `deque`
- `ChainMap`, `OrderedDict`, `namedtuple`

### Module 5 — Object-Oriented Python

[module-05-object-oriented-python/](module-05-object-oriented-python/README.md)

- Classes, objects, attributes, and methods
- Inheritance, composition, encapsulation, polymorphism
- Descriptors and properties
- Class methods and static methods
- Magic methods
- Metaclasses (later)

### Module 6 — Dataclasses

[module-06-dataclasses/](module-06-dataclasses/README.md)

- `@dataclass` and options: `frozen`, `slots`, `order`, `kw_only`
- Comparing dataclass vs `namedtuple` vs attrs vs Pydantic

### Module 7 — Iterators

[module-07-iterators/](module-07-iterators/README.md)

- `__iter__()` and `__next__()`
- Building custom iterators

### Module 8 — Generators

[module-08-generators/](module-08-generators/README.md)

- `yield` and `yield from`
- Generator expressions
- Coroutine basics and lazy evaluation

### Module 9 — Context Managers

[module-09-context-managers/](module-09-context-managers/README.md)

- The `with` statement
- Implementing `__enter__` and `__exit__`
- `contextlib`

### Module 10 — Design Patterns (Pythonic)

[module-10-design-patterns/](module-10-design-patterns/README.md)

Pythonic versions of common patterns — not Java-style memorization.

- Factory, Builder, Strategy, Command
- Observer, State, Adapter, Facade
- Dependency Injection
- Singleton (and why it's often avoided)
- Decorator, Template Method, Visitor (when appropriate)

### Module 11 — Advanced Typing

[module-11-advanced-typing/](module-11-advanced-typing/README.md)

- Generics, Protocols, `TypeVar`, `ParamSpec`
- `TypedDict`, `Literal`, `Self`, `Never`, `Annotated`
- `Union` and `Optional`

### Module 12 — Async Python

[module-12-async-python/](module-12-async-python/README.md)

- `async`, `await`, and `asyncio`
- Tasks, queues, locks, events, semaphores
- Cancellation

### Module 13 — Testing

[module-13-testing/](module-13-testing/README.md)

- `pytest` and `unittest`
- `mock`, fixtures, parameterized tests, coverage

### Module 14 — Packaging

[module-14-packaging/](module-14-packaging/README.md)

- `pyproject.toml`, pip, uv, Poetry, setuptools
- Publishing packages

### Module 15 — Production Quality

[module-15-production-quality/](module-15-production-quality/README.md)

- Logging, configuration, exceptions
- Project layout and dependency injection
- Caching, performance, profiling, benchmarking

---

## Module Folders

| Module | Folder |
|--------|--------|
| 01 — Modern Python | [module-01-modern-python/](module-01-modern-python/README.md) |
| 02 — Functions (Advanced) | [module-02-functions-advanced/](module-02-functions-advanced/README.md) |
| 03 — Functional Python | [module-03-functional-python/](module-03-functional-python/README.md) |
| 04 — Collections | [module-04-collections/](module-04-collections/README.md) |
| 05 — Object-Oriented Python | [module-05-object-oriented-python/](module-05-object-oriented-python/README.md) |
| 06 — Dataclasses | [module-06-dataclasses/](module-06-dataclasses/README.md) |
| 07 — Iterators | [module-07-iterators/](module-07-iterators/README.md) |
| 08 — Generators | [module-08-generators/](module-08-generators/README.md) |
| 09 — Context Managers | [module-09-context-managers/](module-09-context-managers/README.md) |
| 10 — Design Patterns | [module-10-design-patterns/](module-10-design-patterns/README.md) |
| 11 — Advanced Typing | [module-11-advanced-typing/](module-11-advanced-typing/README.md) |
| 12 — Async Python | [module-12-async-python/](module-12-async-python/README.md) |
| 13 — Testing | [module-13-testing/](module-13-testing/README.md) |
| 14 — Packaging | [module-14-packaging/](module-14-packaging/README.md) |
| 15 — Production Quality | [module-15-production-quality/](module-15-production-quality/README.md) |

---

## Lesson Format

Every lesson follows the same [eight-part structure](lesson-structure.md): theory, simple example, professional example, open-source example, common mistakes, best practices, mini challenge, and code review.

---

## Coding Standards

Every piece of code in this repo should:

- Follow PEP 8 formatting
- Use meaningful variable and function names
- Include type hints where appropriate
- Use docstrings for public APIs
- Favor composition over inheritance when practical
- Avoid unnecessary comments; prefer self-explanatory code
- Raise appropriate exceptions rather than returning error codes
- Keep functions focused on a single responsibility
- Prefer explicit behavior over clever tricks
- Write code that is easy to test

### PEPs We Reference

| PEP | Topic |
|-----|-------|
| 8 | Style |
| 20 | Zen of Python |
| 257 | Docstrings |
| 484 | Type hints |
| 526 | Variable annotations |
| 544 | Protocols |
| 557 | Dataclasses |
| 634 | Pattern matching |

We'll also discuss when it's acceptable to deviate from these guidelines and why.

---

## Tools

Tools commonly used in professional Python projects:

| Category | Tool |
|----------|------|
| Formatting | Black |
| Linting | Ruff |
| Type checking | mypy (occasionally pyright) |
| Testing | pytest |
| Package management | uv, pip |
| Documentation | MkDocs or Sphinx (later) |
| Debugging | pdb, `breakpoint()` |

---

## Reading the Standard Library

One of the fastest ways to improve is reading the standard library. We'll study modules such as:

`functools` · `itertools` · `collections` · `pathlib` · `contextlib` · `typing` · `enum` · `abc` · `inspect` · `dataclasses` · `heapq` · `bisect`

---

## Reading Great Open-Source Code

We'll regularly examine projects such as:

Requests · FastAPI · Click · Rich · Typer · Pydantic · CPython (selected files) · Black · Ruff
