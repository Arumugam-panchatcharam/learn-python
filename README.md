# Learning Python

A hands-on repo for learning modern, professional Python through lessons, notes, projects, and tests.

## Repository Layout

```
learn-python/
│
├── README.md
├── pyproject.toml
├── .gitignore
├── LICENSE
├── .python-version               # Optional (for pyenv)
├── .pre-commit-config.yaml        # Later
│
├── notes/
│   ├── lesson01.md
│   ├── lesson02.md
│   └── ...
│
├── lessons/
│   ├── lesson01_advanced_functions/
│   │   ├── theory.py
│   │   ├── examples.py
│   │   ├── exercises.py
│   │   ├── solutions.py
│   │   └── README.md
│   ├── lesson02_decorators/
│   └── ...
│
├── projects/
│   ├── password_manager/
│   ├── todo_cli/
│   ├── file_organizer/
│   ├── mini_http_client/
│   ├── plugin_system/
│   └── ...
│
├── playground/
│   └── scratch.py
│
└── tests/
    ├── test_lesson01.py
    └── ...
```

### Planned Later

- `resources/`
- `benchmarks/`
- `profiling/`
- `design_notes/`
- `open_source_reading/`

---

## How to Use This Repo

1. Read the lesson README in `lessons/lessonNN_<topic>/README.md`.
2. Work through `theory.py` → `examples.py` → `exercises.py`.
3. Compare your work with `solutions.py` after attempting exercises yourself.
4. Capture your understanding in `notes/lessonNN.md`.
5. Run tests with `pytest`.
6. Experiment freely in `playground/scratch.py`.

---

## What Each File Is For

| File | Purpose |
|------|---------|
| `theory.py` | Focused, minimal examples of one concept at a time |
| `examples.py` | Simple → better → professional examples |
| `exercises.py` | Problems only — no solutions |
| `solutions.py` | Polished solutions after review (not first attempts) |
| `README.md` | Learning goals, notes, references, pitfalls — no duplicated code |
| `notes/lessonNN.md` | Your personal study notes and reflections |

This split lets you compare your first attempt with an improved version.

---

## Lesson Index

| # | Lesson | Code | Notes | Status |
|---|--------|------|-------|--------|
| 01 | Advanced Functions | [lessons/lesson01_advanced_functions/](lessons/lesson01_advanced_functions/README.md) | [notes/lesson01.md](notes/lesson01.md) | Started |
| 02 | Decorators | [lessons/lesson02_decorators/](lessons/lesson02_decorators/README.md) | [notes/lesson02.md](notes/lesson02.md) | Planned |
| 03 | Functools | [lessons/lesson03_functools/](lessons/lesson03_functools/README.md) | [notes/lesson03.md](notes/lesson03.md) | Planned |
| 04 | Iterators | [lessons/lesson04_iterators/](lessons/lesson04_iterators/README.md) | [notes/lesson04.md](notes/lesson04.md) | Planned |
| 05 | Generators | [lessons/lesson05_generators/](lessons/lesson05_generators/README.md) | [notes/lesson05.md](notes/lesson05.md) | Planned |
| 06 | Classes | [lessons/lesson06_classes/](lessons/lesson06_classes/README.md) | [notes/lesson06.md](notes/lesson06.md) | Planned |
| 07 | Dataclasses | [lessons/lesson07_dataclasses/](lessons/lesson07_dataclasses/README.md) | [notes/lesson07.md](notes/lesson07.md) | Planned |
| 08 | Collections | [lessons/lesson08_collections/](lessons/lesson08_collections/README.md) | [notes/lesson08.md](notes/lesson08.md) | Planned |
| 09 | Context Managers | [lessons/lesson09_context_managers/](lessons/lesson09_context_managers/README.md) | [notes/lesson09.md](notes/lesson09.md) | Planned |
| 10 | Design Patterns | [lessons/lesson10_design_patterns/](lessons/lesson10_design_patterns/README.md) | [notes/lesson10.md](notes/lesson10.md) | Planned |

**Foundations:** [Naming appendix](notes/appendix-naming.md)

---

## Projects

Capstone-style projects to apply multiple lessons:

| Project | Folder | Status |
|---------|--------|--------|
| Password Manager | [projects/password_manager/](projects/password_manager/README.md) | Planned |
| Todo CLI | [projects/todo_cli/](projects/todo_cli/README.md) | Planned |
| File Organizer | [projects/file_organizer/](projects/file_organizer/README.md) | Planned |
| Mini HTTP Client | [projects/mini_http_client/](projects/mini_http_client/README.md) | Planned |
| Plugin System | [projects/plugin_system/](projects/plugin_system/README.md) | Planned |

---

## Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dev tools
pip install -e ".[dev]"

# Run tests
pytest

# Lint and format
ruff check .
ruff format .
```

---

## Coding Standards

- Follow PEP 8 formatting
- Use meaningful names and type hints where appropriate
- Use docstrings for public APIs
- Favor composition over inheritance when practical
- Raise appropriate exceptions rather than returning error codes
- Keep functions focused on a single responsibility
- Write code that is easy to test

### Tools

| Category | Tool |
|----------|------|
| Formatting | Ruff |
| Linting | Ruff |
| Type checking | mypy |
| Testing | pytest |
| Package management | pip / uv |

---

## Commit Style

Practice conventional, descriptive commit messages:

```
feat: add lesson 01 examples
refactor: simplify closure example
style: format code with Ruff
test: add iterator unit tests
docs: explain positional-only parameters
fix: handle empty iterable
```

| Prefix | Use for |
|--------|---------|
| `feat` | New lesson content, examples, or project features |
| `refactor` | Code restructuring without behavior change |
| `style` | Formatting and lint fixes |
| `test` | Adding or updating tests |
| `docs` | README, notes, and lesson documentation |
| `fix` | Bug fixes in examples, solutions, or projects |

---

## Reading List

**Standard library:** `functools` · `itertools` · `collections` · `pathlib` · `contextlib` · `typing` · `enum` · `dataclasses`

**Open source:** Requests · FastAPI · Click · Rich · Typer · Pydantic · Black · Ruff
