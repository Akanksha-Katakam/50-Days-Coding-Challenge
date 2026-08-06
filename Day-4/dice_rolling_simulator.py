# Day - 4 -> Dice Rolling Simulator

import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)


while True:
    print("\nDice Rolling Simulator")

    input("Press Enter to Roll the Dice...")

    number = roll_dice()

    print("You rolled:", number)

    choice = input("\nRoll Again? (yes/no): ").lower()

    if choice == "no":
        print("Thank you for playing!")
        break