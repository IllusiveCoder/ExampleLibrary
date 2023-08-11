# Guess the Number Game

'''This program implements a simple guessing game 
where the computer generates a random number, and 
the user tries to guess it. The program provides hints 
to guide the user toward the correct guess.'''

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Number of attempts
attempts = 0

print("Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

# Game loop
while True:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
