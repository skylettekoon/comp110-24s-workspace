"""Functional Battleship."""

__author__ = "730559378"
import random

secret_row: int = 3
secret_column: int = 2

# Declaring input_guess function


def input_guess(grid_size: int, row_column_guess: str) -> int:
    """Returns the row or column guess."""
    assert row_column_guess == "row" or row_column_guess == "column"
    row_or_column_guess: int = int(input(f"Guess a {row_column_guess}: "))
    # Gives a "Try Again" message if guess is outside grid size
    while (int(row_or_column_guess) > grid_size) or (int(row_or_column_guess) < 1):
        row_or_column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return row_or_column_guess

# Declaring print_grid function


def print_grid(grid_size: int, row_guess: int, column_guess: int, if_correct: bool) -> None:
    """Prints Box Grid to Represent Game Board."""
    # Box codes
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    # Printing Red Box for Correct and White Box for Incorrect
    result: str
    if if_correct is True:
        result = RED_BOX
    else: 
        result = WHITE_BOX
    row_counter: int = 1
    while row_counter <= grid_size:
        emoji_string: str = ""
        column_counter: int = 1
        if row_counter == row_guess:
            while column_counter <= grid_size:
                if column_counter == column_guess:
                    emoji_string += result
                else:   # Printing Blue Box for Unguessed Locations
                    emoji_string += BLUE_BOX
                column_counter += 1
        else:   # Printing Blue Box for Unguessed Locations
            while column_counter <= grid_size: 
                emoji_string += BLUE_BOX
                column_counter += 1

        print(emoji_string)   
        row_counter += 1         

# Declaring correct_guess function 


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Evaluating Guesses as True or False."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:   # Secret_row != row_guess or secret_column != column_guess
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Putting together all functions!"""
    player_turn: int = 1
    # Giving Player 5 turns to get correct guesses
    while player_turn <= 5:
        print(f"=== Turn {player_turn}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        hit_or_miss: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        # Player was correct; game over
        if hit_or_miss is True:
            print_grid(grid_size, row_guess, column_guess, True)
            print("Hit!")
            print(f"You won in {player_turn}/5 turns!")
            return
        # Player was incorrect
        else:   # Correct_guess == False
            print_grid(grid_size, row_guess, column_guess, False)
            print("Miss!")
            player_turn += 1
        
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))