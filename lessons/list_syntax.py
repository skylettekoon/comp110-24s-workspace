"""Demonstrate Basic List Syntax"""

# Initialize an empty list
grocery_list: list[str] = list() # <- List constructor
grocery_list: list[str] = [] # <- literal

#Adding Items to List
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

#Create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list:")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

#Indexing
print("Print first element of string")
print(grocery_list[0])

# Modifying by Index
print("Before changes: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change")
print(grocery_list)

# Measuring length of list
print(len(grocery_list))

# Removing an item
grocery_list.pop(1)
print("After removing almond milk")
print(grocery_list)

# Function name: display
# Parameter: list[str]
# Return nothing
# Print list

def display(word: list[str]) -> None:
    print(word)

display(grocery_list)

# Create list
# Name: create
# Parameter: str and str
# Return value: list[str]
# Put both parameters into a list

def create(item1: str, item2: str) -> list[str]:
    print(f"{item1}, {item2}")

create("cookies", "milk")
