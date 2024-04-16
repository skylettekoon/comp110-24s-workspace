"""Exercise 4."""

__author__ = "730559378"


def all(list: list[int], choosen: int) -> bool:
    """Check if the ints in given list are the same as the given."""
    index = 0
    list_length = len(list)
    if list_length == 0:
        return False
    while index < list_length:
        if list[index] != choosen:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Returns largest value in list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = 1
    max_value = input[0]
    length = len(input)
    while index < length:
        if input[index] > max_value:
            max_value = input[index]
        index += 1
    return max_value
    

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists have the same values."""
    index = 0
    length1 = len(list1)
    length2 = len(list2)
    if length1 != length2:
        return False
    while index < length1:
        if list1[index] != list2[index]:
            return False
        index += 1
    return True
    

def extend(list1: list[int], list2: list[int]) -> None:
    """Adds list 1 to list 2."""
    index = 0
    length = len(list2)
    while index < length:
        list1.append(list2[index])
        index += 1