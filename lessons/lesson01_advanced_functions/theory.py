"""Focused examples for advanced functions."""


def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"


def apply_twice(func, value):
    """Call `func` twice on `value`."""
    return func(func(value))


def make_multiplier(factor: int):
    """Return a function that multiplies by `factor`."""

    def multiply(value: int) -> int:
        return value * factor

    return multiply
