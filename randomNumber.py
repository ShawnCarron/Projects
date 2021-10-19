# Import Modules
import random

print("We are going to play a guessing game.")
top_of_range = input("Type a number between 1 and 100: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    print(f"I am thinking of a number between 1 and {top_of_range}.")

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number: ')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess which number I am thinking of: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("I am thinking of a number, not a letter. Try Again.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Too high!")
    else:
        print("Too low!")

print("You got it in", guesses, "guesses.")

