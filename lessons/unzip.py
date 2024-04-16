"""Splitting a dictionary into two lists."""

__author__ = "730559378"


def get_keys(test: dict[str, int]) -> list[str]:
    """Moves keys in dictionary to list."""
    new_list: list[str] = list()
    if len(test) == 0:
        return new_list
    for key in test:
        new_list.append(key)
    return new_list


def get_values(test2: dict[str, int]) -> list[int]:
    """Moves values in dictionary to list."""
    new_list2: list[int] = list()
    if len(test2) == 0:
        return new_list2
    for key in test2:
        new_list2.append(test2[key])
    return new_list2
    