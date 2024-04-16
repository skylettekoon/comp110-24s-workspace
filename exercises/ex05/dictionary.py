"""Exercise 5: Dictionary functions."""

__author__ = "730559378"


def invert(cookie: dict[str, str]) -> dict[str, str]:
    """Inverts key and value."""
    pie = {}
    for key in cookie:
        if cookie[key] in pie:
            raise KeyError("Duplicate spotted!")
        else:
            pie[cookie[key]] = key
    return pie


def favorite_color(colors: dict[str, str]) -> str:
    """Returns most common color."""
    max_color: dict[str, int] = {}
    value = 0
    for key in colors:
        # Color has been encountered already; add one to count
        if colors[key] in max_color:
            max_color[colors[key]] += 1
        else:  # first time encountering color
            max_color[colors[key]] = 1 
    for key in max_color:
        if max_color[key] > value:
            popular_color: str = str(key)
            value = max_color[key]
    return popular_color


print(favorite_color({"A": "yellow", "B": "green", "C": "blue", "D": "blue", "E": "green"}))  


def count(freq_list: list[str]) -> dict[str, int]:
    """Counts frequency of items in a list."""
    result_dict: dict[str, int] = {}
    for item in freq_list:
        # Item already in dictionary; add one to count
        if item in result_dict:
            result_dict[item] += 1
        else:  # Item not in dictionary; start count for item
            result_dict[item] = 1
    return result_dict


def alphabetizer(abc_list: list[str]) -> dict[str, list[str]]:
    """Alphabetizes a list of words."""
    ordered_dict: dict[str, list[str]] = {}
    for word in abc_list:
        # Checking if letter is already in dictionary
        if word[0].lower() in ordered_dict:
            ordered_dict[word[0].lower()].append(word)
        else:  # Adds word to a new list with the new letter
            ordered_dict[word[0].lower()] = [word]
    return ordered_dict
          

def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance."""
    # Adds student to attendance for day of the work.
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:  # day of the week not already in dictionary.
        attendance[day] = [student]
    return


attendance: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance, "Tuesday", "Vrinda")
update_attendance(attendance, "Wednesday", "Kaleb")
print(attendance)