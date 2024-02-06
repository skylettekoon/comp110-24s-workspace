"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730559378"

# Box Codes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Player One Picks A Location

user_number: int = int(input("Pick a secret boat location between 1 and 4: "))
if (user_number < 1):
    print(f"Error! {user_number} too low!")
    exit()
if (user_number > 4):
    print(f"Error! {user_number} too high!")
    exit()
    
# Player Two Guess's and Whether They Are Correct
    
user_input: int = int(input("Guess a number between 1 and 4: "))
if (user_input < 1):
    print(f"Error! {user_input} too low!")
    exit()
if (user_input > 4):
    print(f"Error! {user_input} too high!")
    exit()
if (user_input == 1) and (user_number == 1):
    print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    print("Correct! You hit the ship.")
if (user_input == 1) and (user_number != 1):
    print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    print("Incorrect! You missed the ship.")
if (user_input == 2) and (user_number == 2):
    print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    print("Correct! You hit the ship.")
if (user_input == 2) and (user_number != 2):
    print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
    print("Incorrect! You missed the ship.")
if (user_input == 3) and (user_number == 3):
    print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    print("Correct! You hit the ship.")
if (user_input == 3) and (user_number != 3):
    print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
    print("Incorrect! You missed the ship.")
if (user_input == 4) and (user_number == 4):
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    print("Correct! You hit the ship.")
if (user_input == 4) and (user_number != 4):
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
    print("Incorrect! You missed the ship.")    