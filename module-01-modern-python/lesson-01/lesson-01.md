# Lesson 01 — Naming

**Module:** Modern Python  
**Topics:** Variables, functions, classes, constants, and module naming conventions

---

## Part 1 — Theory

Good naming is one of the highest-leverage skills in Python. Names are documentation: they tell readers what a value represents, what a function does, and how a class should be used.

Python follows **PEP 8** naming conventions:

| Kind | Convention | Example |
|------|------------|---------|
| Variables | `snake_case` | `user_count` |
| Functions | `snake_case` | `calculate_total()` |
| Methods | `snake_case` | `get_user()` |
| Classes | `CapWords` (PascalCase) | `UserAccount` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES` |
| Modules | `snake_case` (short, lowercase) | `user_service.py` |
| Private (by convention) | leading `_` | `_internal_cache` |

Names should be **descriptive**, not abbreviated unless the abbreviation is widely understood (`http`, `id`, `url`). Avoid single-letter names except for trivial loop counters (`i`, `j`) or well-known math (`x`, `y` in coordinate systems).

Boolean names should read as questions: `is_active`, `has_permission`, `can_edit`.

---

## Part 2 — Simple Example

```python
# Poor naming
def f(x, y):
    return x * y

# Better naming
def calculate_area(width: float, height: float) -> float:
    return width * height
```

```python
# Poor naming
d = {"n": "Alice", "a": 30}

# Better naming
user = {"name": "Alice", "age": 30}
```

---

## Part 3 — Professional Example

```python
from dataclasses import dataclass
from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


@dataclass(frozen=True)
class ShippingAddress:
    street: str
    city: str
    postal_code: str


def is_order_eligible_for_refund(
    status: OrderStatus,
    days_since_delivery: int,
    max_refund_window_days: int = 30,
) -> bool:
    """Return True if the order can still be refunded."""
    if status is not OrderStatus.DELIVERED:
        return False
    return days_since_delivery <= max_refund_window_days
```

Notice how each name answers a question: *What is this?* *What does this function return?* *What are the units?*

---

## Part 4 — Open-Source Example

Study naming in the [Requests](https://github.com/psf/requests) library:

- `requests.get()` — verb matches HTTP action
- `response.status_code` — noun phrase, not `sc` or `code`
- `response.raise_for_status()` — reads like English

Open `requests/models.py` and notice how class names (`PreparedRequest`, `Response`) and method names (`prepare_headers`, `iter_content`) stay consistent across the codebase.

---

## Part 5 — Common Mistakes

1. **Abbreviating too aggressively** — `usr_cnt` instead of `user_count`
2. **Hungarian notation** — `strName`, `intCount` (not idiomatic in Python)
3. **Misleading names** — a function called `get_user` that also deletes the user
4. **Shadowing builtins** — naming a variable `list`, `dict`, or `id`
5. **Inconsistent style** — mixing `getUserData` and `get_user_data` in the same project
6. **Overly generic names** — `data`, `info`, `temp`, `result` in wide scopes

---

## Part 6 — Best Practices

- Name functions and methods after **what they do**, not how they do it
- Use verbs for functions (`fetch_users`, `validate_email`) and nouns for data (`email_address`)
- Keep names **searchable** — avoid `e`, `n`, `tmp` in non-trivial code
- Match the **scope** — short names in tiny scopes, longer names in larger scopes
- Rename when understanding changes; good names evolve with the code
- Run a linter (Ruff) to catch naming issues early

---

## Part 7 — Mini Challenge

Refactor this code with better names. Do not change behavior.

```python
def p(d, t):
    r = []
    for i in d:
        if i["t"] == t:
            r.append(i["n"])
    return r


data = [
    {"n": "widget", "t": "tool", "p": 9.99},
    {"n": "hammer", "t": "tool", "p": 14.50},
    {"n": "apple", "t": "food", "p": 1.20},
]

print(p(data, "tool"))
```

**Goal:** Every name should make the code readable without comments.

---

## Part 8 — Code Review

A strong refactor:

```python
from typing import Any


def get_product_names_by_type(
    products: list[dict[str, Any]],
    product_type: str,
) -> list[str]:
    matching_names = []
    for product in products:
        if product["type"] == product_type:
            matching_names.append(product["name"])
    return matching_names


products = [
    {"name": "widget", "type": "tool", "price": 9.99},
    {"name": "hammer", "type": "tool", "price": 14.50},
    {"name": "apple", "type": "food", "price": 1.20},
]

print(get_product_names_by_type(products, "tool"))
```

**What improved:**

- Function name describes the operation and return value
- Parameter names replace cryptic `d` and `t`
- Dictionary keys are spelled out (`name`, `type`, `price`)
- Intermediate variable `matching_names` clarifies intent

**Next step:** In a later lesson, replace `dict[str, Any]` with a `@dataclass` or `TypedDict`.

---

**Next lesson:** [Lesson 02 — Imports](../../module-01-modern-python/lesson-02/lesson-02.md)