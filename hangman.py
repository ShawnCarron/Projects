import random
import time

def intro():
    print("Welcome to Hangman by Cyberphreak Studios.")
    name = input("Please introduce yourself: ")
    print("Welcome, " + name + " I hope you are you ready to play! ")
    time.sleep(2)
    print("The game is about to begin!\nLet's play Hangman!")
    time.sleep(2)

def main():
    global count 
    global display
    global word 
    global alreadyGuessed
    global length
    global playGame
    wordsToGuess = ["january","border","image","film","promise","kids","lungs","doll", "layne"]
    word = random.choice(wordsToGuess)
    length = len(word)
    count = 0
    display = '_' * length
    alreadyGuessed = []
    playGame = ""

# A loop to re-execute the game when the first round ends:
def play_loop():
    global playGame
    playGame = input("Do You want to play again? y = yes, n = no \n").lower()
    while playGame not in ["y", "n", "N", "Y", "yes", "no"]:
        playGame = input("Do You want to play again? y = yes, n = no \n").lower()
    if playGame == "y" or "yes":
        main()
    elif playGame == "n" or "no":
        print("Thanks For Playing! We expect you back again!")
        exit() 
        
# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global alreadyGuessed
    global playGame
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        alreadyGuessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in alreadyGuessed:
        print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",alreadyGuessed,word)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()

intro()
main()
hangman()