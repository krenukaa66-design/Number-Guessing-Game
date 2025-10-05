
import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

number_guessing_game()
