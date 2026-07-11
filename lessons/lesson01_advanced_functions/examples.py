"""Progressively better examples for advanced functions."""


# Simple example

def summarize(*values: int) -> int:
    return sum(values)


# Better example

def build_query(table: str, *columns: str, **filters: str) -> str:
    selected = ", ".join(columns) if columns else "*"
    where = " AND ".join(f"{key} = {value!r}" for key, value in filters.items())
    if where:
        return f"SELECT {selected} FROM {table} WHERE {where}"
    return f"SELECT {selected} FROM {table}"


# Professional example

from collections.abc import Callable


def with_logging(func: Callable[..., int]) -> Callable[..., int]:
    """Wrap a numeric function with basic logging."""

    def wrapper(*args: int, **kwargs: int) -> int:
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args}, {kwargs}) -> {result}")
        return result

    return wrapper
