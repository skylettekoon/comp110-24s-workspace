"""Summing the elements of a list using different loops."""

__author__ = "730559378"


def w_sum(vals: list[float]) -> float:
    """Part 1."""
    if len(vals) == 0:
        return float(0.0)
    idx: int = 0
    final_value: float = 0.0
    while idx < len(vals):
        first = vals[idx]
        final_value = final_value + first
        idx = idx + 1
    return final_value


def f_sum(vals: list[float]) -> float:
    """Part 2."""
    if len(vals) == 0:
        return float(0.0)
    final_value: float = 0.0
    for elem in vals:
        final_value += elem
    return final_value
    

def f_range_sum(vals: list[float]) -> float:
    """Part 3."""
    final_value: float = 0.0
    if len(vals) == 0:
        return float(0.0)
    for index in range(0, len(vals)): 
        final_value += vals[index]
    return final_value
