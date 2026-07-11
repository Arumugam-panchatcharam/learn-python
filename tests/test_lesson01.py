"""Tests for lesson 01."""

import pytest

from lessons.lesson01_advanced_functions.solutions import calculate


def test_calculate_success() -> None:
    assert calculate("add", 1, 2) == 3
    assert calculate("subtract", 1, 2) == -1
    assert calculate("multiply", 1, 2) == 2
    assert calculate("divide", 1, 2) == 0.5


def test_calculate_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate("divide", 1, 0)


def test_calculate_invalid_operation() -> None:
    with pytest.raises(ValueError, match="Invalid operation: invalid"):
        calculate("invalid", 1, 2)


def test_calculate_invalid_arguments() -> None:
    with pytest.raises(ValueError, match=r"Invalid arguments: 1 and 2"):
        calculate("add", "1", 2)
