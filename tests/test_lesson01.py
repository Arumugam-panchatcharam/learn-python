"""Tests for lesson 01."""

from lessons.lesson01_advanced_functions.theory import greet, make_multiplier
from lessons.lesson01_advanced_functions.solutions import merge_counts, make_formatter, repeat


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_make_multiplier() -> None:
    double = make_multiplier(2)
    assert double(5) == 10


def test_make_formatter() -> None:
    warn = make_formatter("WARN")
    assert warn("disk full") == "WARN: disk full"


def test_merge_counts() -> None:
    assert merge_counts({"a": 1, "b": 2}, {"b": 3}) == {"a": 1, "b": 5}


def test_repeat() -> None:
    assert repeat(lambda value: value + 1, 3, 0) == 3
