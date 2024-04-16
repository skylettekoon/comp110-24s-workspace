"""test sum functionality."""

from lessons.sum2 import sum

def test_sum_empty() -> None:
    """Sum of empty list should return 0."""
    assert sum([]) == 0


def test_sum_one_element() -> None:
    """Sum of one element should return that element."""
    test: list[int] = [7]
    assert sum(test) == 7


def test_sum_positive() -> None:
    """Sum of postive numbers should return sum of those numbers."""
    test: list[int] = [2,4,6]
    assert sum(test) == 12


def test_sum_with_negatives() -> None:
    """Sum should work with positives and negative numbers."""
    test: list[int] = [2, -2, 4]
    assert sum(test) ==4