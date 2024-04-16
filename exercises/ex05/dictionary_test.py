"""Testing functions from the dictionary exercises."""

__author__ = "730559378"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

# Tests for invert function


def test_invert_use1() -> None:
    """Asserts that key and value are inverted."""
    cookie: dict[str, str] = {'red': 'blue'}
    return_dict: dict[str, str] = invert(cookie)
    assert return_dict == {'blue': 'red'}


def test_invert_use2() -> None:
    """Checks that returned list has the same amount of items as the original."""
    cookie: dict[str, str] = {'red': 'blue'}
    return_dict: dict[str, str] = invert(cookie)
    assert len(cookie) == len(return_dict)


def test_invert_edge() -> None:
    """Tests that an empty dictionary returns if the original dictionary is empty."""
    cookie: dict[str, str] = {}
    return_dict: dict[str, str] = invert(cookie)
    assert return_dict == {}


# Tests for favorite color function
    

def test_favorite_color_use1() -> None:
    """Assert that the max color in a dictionary is returned."""
    max_color: dict[str, str] = {'Skylette': 'blue', 'Maria': 'green', 'Tejas': 'purple', 'Adele': 'blue'}
    popular_color: str = favorite_color(max_color)
    assert popular_color == 'blue'


def test_favorite_color_use2() -> None:
    """Assert that when there is a tie, the first color that appears is returned."""
    max_color: dict[str, str] = {'Skylette': 'blue', 'Maria': 'green', 'Tejas': 'green', 'Adele': 'blue'}
    popular_color: str = favorite_color(max_color)
    assert popular_color == 'blue'


def test_favorite_color_edge() -> None:
    """If everyone has the same favorite color, it still returns that color."""
    max_color: dict[str, str] = {'Skylette': 'blue', 'Maria': 'blue', 'Tejas': 'blue', 'Adele': 'blue'}
    popular_color: str = favorite_color(max_color)
    assert popular_color == 'blue'


# Tests for count function
    
def test_count_use1() -> None:
    """Returns the correct frequency."""
    freq_list: list[str] = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result_dict: dict[str, int] = count(freq_list)
    assert result_dict == {'apple': 3, 'banana': 2, 'orange': 1}


def test_count_use2() -> None:
    """The length of the list should be the same as the sum of the values in the dictionary."""
    freq_list: list[str] = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result_dict: dict[str, int] = count(freq_list)
    item_counter = 0
    for key in result_dict:
        item_counter += result_dict[key]
    assert item_counter == len(freq_list)


def test_count_edge() -> None:
    """The value in the dictionary should not be a float."""
    freq_list: list[str] = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result_dict: dict[str, int] = count(freq_list)
    assert result_dict != dict[str, float]
  

# Tests for alphabetizer function
    

def test_alphabetizer_use1() -> None:
    """The words should be alphabetized."""
    abc_list: list[str] = ['dolphin', 'cheetah', 'lion', 'dog']
    ordered_dict: dict[str, list[str]] = alphabetizer(abc_list)
    assert ordered_dict == {'d': ['dolphin', 'dog'], 'c': ['cheetah'], 'l': ['lion']}


def test_alphabetizer_use2() -> None:
    """Whether a word is captilized or not should not matter."""
    abc_list: list[str] = ['dolphin', 'Cheetah', 'Lion', 'dog']
    ordered_dict: dict[str, list[str]] = alphabetizer(abc_list)
    assert ordered_dict == {'d': ['dolphin', 'dog'], 'c': ['Cheetah'], 'l': ['Lion']}


def test_alphabetizer_edge() -> None:
    """An empty list returns an empty dictionary."""
    abc_list: list[str] = []
    ordered_dict: dict[str, list[str]] = alphabetizer(abc_list)
    assert ordered_dict == {}


# Tests for update attendance function
    

def test_update_attendance_use1() -> None:
    """Student is added to day they attended."""
    attendance: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Tuesday"
    student: str = "Allie"
    update_attendance(attendance, day, student)
    assert attendance == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Allie"]}


def test_update_attendance_use2() -> None:
    """Day of the week is added if not already listed."""
    attendance: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Wednesday"
    student: str = "Allie"
    update_attendance(attendance, day, student)
    assert attendance == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["Allie"]}


def test_update_attendance_edge() -> None:
    """Tests if the dictionary is empty."""
    attendance: dict[str, list[str]] = {}
    day: str = "Friday"
    student: str = "Sophie"
    update_attendance(attendance, day, student)
    assert attendance == {"Friday": ["Sophie"]}