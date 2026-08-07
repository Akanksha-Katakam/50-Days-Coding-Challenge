# Day - 5 -> Number Guessing Game

import random

def generate_number():
    return random.randint(1, 100)


while True:

    secret_number = generate_number()
    attempts = 0
    max_attempts = 7

    print("\n===== Number Guessing Game =====")
    print("Guess a number between 1 and 100")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:

        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\n Congratulations!")
            print("You guessed the correct number.")
            print("Attempts:", attempts)
            break

    else:
        print(f"\nGame Over! The number was {secret_number}")

    choice = input("\nPlay Again? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for playing!")
        break