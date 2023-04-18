import random
from art import logo


def guessing_number(level_dificulty):
    attempts = 5 if level_dificulty == "hard" else 10

    play = True
    guessing_number = random.randint(1, 100)


    print(f"The correct answer - {guessing_number}")
    while play:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == guessing_number:
            print(f"You got it! The answer was {guessing_number}")
            play = False
        elif guess < guessing_number:
            print("Too low.\nGuess again.")
            attempts -= 1
        else:
            print("Too high.\nGuess again.")
            attempts -= 1




print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()

guessing_number(level)