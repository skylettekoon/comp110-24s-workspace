"""One Shot Battleship Exercise."""

__author__ = "730559378"

secret_row: int = 3
secret_column: int = 2
grid_size: int = 4

# Box codes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Guessing a Row
row_guess: int = (int)(input("Guess a row: "))
while (int(row_guess) > grid_size) or (int(row_guess) < 1):
    row_guess = (int)(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    
# Guessing a Column
    
column_guess: int = (int)(input("Guess a column: "))
while (int(column_guess) > grid_size) or (int(column_guess) < 1):
    column_guess = (int)(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

result: str = ""
row_counter: int = 1
# Building Emoji Grid Based on Correctness of Row and Column Guess
while row_counter <= grid_size:
    emoji_string = ""
    column_counter: int = 1
    # Red box means correct. White box means incorrect. 
    if row_counter == row_guess:
        while column_counter <= grid_size:
            if column_guess == column_counter:
                if column_guess == secret_column and row_guess == secret_row:
                    result += RED_BOX
                    emoji_string += result
                else:   # Row guess and/or column guess are incorrect; print white box
                    result += WHITE_BOX
                    emoji_string += result
            else:   # Printing blue boxes for unguessed locations
                emoji_string += BLUE_BOX
            column_counter += 1
    else:   # Printing blue boxes for unguessed locations
        while column_counter <= grid_size:
            emoji_string += BLUE_BOX
            column_counter += 1
    print(emoji_string)
    row_counter += 1
# Printed Feedback
if int(column_guess) == secret_column and int(row_guess) == secret_row:
    print("Hit!")
else:
    if int(column_guess) == secret_column and int(row_guess) != secret_row:
        print("Close! Correct column, wrong row.")
    if int(column_guess) != secret_column and int(row_guess) == secret_row:
        print("Close! Correct row, wrong column.")
    if int(column_guess) != secret_column and int(row_guess) != secret_row:
        print("Miss!")