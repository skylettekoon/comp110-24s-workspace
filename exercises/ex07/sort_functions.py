"""Functions that implement sorting algorithms."""

__author__ = "730559378"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sorted_index = 0
    while sorted_index < len(x) - 1:
        unsorted_index = sorted_index + 1
        current = x[unsorted_index]
        while unsorted_index > 0 and current < x[unsorted_index - 1]:
            temp_value = x[unsorted_index]
            x[unsorted_index] = x[unsorted_index - 1]
            x[unsorted_index - 1] = temp_value
            unsorted_index -= 1
        sorted_index += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    counter = 0
    while counter < len(x):
        min_value = counter
        index_counter = counter + 1
        while index_counter < len(x):
            if x[index_counter] < x[min_value]:
                min_value = index_counter
            index_counter += 1
        
        temp_value = x[counter]
        x[counter] = x[min_value]
        x[min_value] = temp_value
        counter += 1
    return None
    