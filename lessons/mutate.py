"""Mutating functions."""

__author__ = "730559378"


def manual_append(word1: list[int], word2: int) -> None:
    """Appends int to end of list."""
    word1.append(word2)
    return


def double(word1: list[int]) -> None:
    """Doubles items in list."""
    index = 0
    while index < len(word1):
        word1[index] *= 2
        index += 1
    print(word1)
