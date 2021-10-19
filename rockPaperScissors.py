import random

userWins = 0
computerWins = 0
options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if userInput == "q":
        break

    if userInput not in options:
        continue

    randomNumber = random.randint(0, 2)
    computerPick = options[randomNumber]
    print("The computer picked", computerPick + ".")

    if userInput == "rock" and computerPick == "scissors":
        print("You won!")
        userWins += 1

    elif userInput == "paper" and computerPick == "rock":
        print("You won!")
        userWins += 1

    elif userInput == "scissors" and computerPick == "paper":
        print("You won!")
        userWins += 1

    else:
        print("You lost!")
        computerWins +=1

print("You won", userWins, 'times.')
print("The computer won", computerWins, "times.")

if computerWins > userWins:
    print("The computer got the better of you!")
elif computerWins == userWins:
    print("You tied!")
else:
    print("You rocked the j00b0x!")
print("Goodbye!")