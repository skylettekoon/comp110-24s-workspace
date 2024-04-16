"""Challenge question: Recursions."""

__author__ = "730559378"


def f(n: int, k: int) -> int:
    """Multiplies two integers."""
    if n == 0:
        return 0
    else:
        return n * k