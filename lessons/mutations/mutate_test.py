"""Test my mutating_functions."""

from lessons.mutations.mutating_functions import remove_first, get_first, get_and_remove_first

def test_remove_first_use_case() -> None:
    """Test basic use case for remove_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    remove_first(t)
    assert t == ["rainy", "sunny"]