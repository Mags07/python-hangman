'''
imports
'''
import random
import hangman_picture
from words import words


'''
Title
'''
print("Welcome to Hangman Game")

'''
Rules of the game
'''
print("Rules; Hangman is a simple word guessing game.")
print("You have 6 chances to guess all the letters in the unknown word.")
print("If you guess all the letters before your 6 chances are use, you win!")
print("If you use up all your chances, you are hanged!")
print("Good luck!")
print("Press P or p to start the game")


'''
Computer randomly selects the hangman word.
'''
def select_word(words):
    return random.choice(words)


'''
The chosen word shows up as dashes while they have not been guessed.
'''
def print_hangman_word(hangman_word):
    print(" _ " * len(hangman_word))


'''
Check if guessed letter is in the work and to not allow user to guess anything except a single letter.
'''
def letter_input_correct(choice, hangman_word):
    if len(choice) > 1 or not choice.isalpha():
        print("You can only pick a single letter. Try again - \n")
        sys.exit()
    else:
        if choice in hangman_word:
            return True
        else:
            return False


'''
Keeping track of guest's remaining guesses and which letters they have used up.
'''
remaining_attempts = 6
guessed_letters = ""
hangman_word = select_word(words)
choice = input("Pick a letter - \n")
print(hangman_picture.get_hangman_picture(remaining_attempts))
print_hangman_word(hangman_word)
input_in_hangman_word = letter_input_correct(choice, hangman_word)