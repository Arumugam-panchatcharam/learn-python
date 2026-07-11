"""Polished solutions for advanced functions."""


from collections.abc import Callable


def repeat(callable_: Callable[[int], int], times: int, value: int) -> int:
    result = value
    for _ in range(times):
        result = callable_(result)
    return result


def make_formatter(prefix: str) -> Callable[[str], str]:
    def format_message(message: str) -> str:
        return f"{prefix}: {message}"

    return format_message


def merge_counts(*counters: dict[str, int]) -> dict[str, int]:
    merged: dict[str, int] = {}
    for counter in counters:
        for key, value in counter.items():
            merged[key] = merged.get(key, 0) + value
    return merged
