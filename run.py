# imports
import random
import hangman_picture
import sys
from words import words


def introduction():
    # Title
    print("Welcome to Hangman Game")

    # Rules of the game
    print("Rules; Hangman is a simple word guessing game.")
    print("You have 6 chances to guess all the letters in the unknown word.")
    print("If you guess all the letters, you win!")
    print("If you use up all your chances, you are hanged!")
    print("Good luck!")
    name = ""
    while not name.isalpha():
        name = input("What is your name? (Use letters only): \n")
        if name.isalpha():
            print("Welcome {}! Start the game!".format(name))


# Computer randomly selects the hangman word.
def select_word(words):
    return random.choice(words)


# The chosen word shows up as dashes while they have not been guessed.
def print_hangman_word(hangman_word, guessed_letters):
    for letter in hangman_word:
        if letter.upper() in guessed_letters.upper():
            print("{}".format(letter), end="")
        else:
            print(" _ ", end="")
    print("\n")


# Check if guessed letter is in word & block double letters, numbers or signs
def letter_input_correct(choice, hangman_word):
    if len(choice) > 1 or not choice.isalpha():
        print("You can only pick a single letter. Try again: \n")
        sys.exit()
    else:
        if choice.lower() in hangman_word.lower():
            return True
        else:
            return False


def characters(word):
    return "".join(set(word))

# Keeping track of guest's remaining guesses & which letters they have used up


guessed_letters = ""
hangman_word = select_word(words)
chances_left = 6
introduction()

while chances_left > 0 and len(guessed_letters) < len(characters(hangman_word)):
    choice = input("Pick a letter: \n")
    if choice.lower() not in guessed_letters.lower():
        guessed_letters += choice
    input_in_hangman_word = letter_input_correct(choice, hangman_word)
    if input_in_hangman_word:
        if choice in guessed_letters:
            print("You already guessed this letter. Pick another")
        else:
            print("You were right! That letter is part of the word.")
    else:
        print("Unfortunately that letter is not part of the word.")
        chances_left -= 1

    print(hangman_picture.get_hangman_picture(chances_left))
    print("\n{} attempts left".format(chances_left))
    print_hangman_word(hangman_word, guessed_letters)
    print("\n\nNumber of letters guessed:{}\n".format(len(guessed_letters)))


guessed_word = ""
for letter in hangman_word:
    if letter.lower() in guessed_letters.lower():
        guessed_word += letter

# Result of the game
if guessed_word.upper() == hangman_word.upper():
    print("Congratulations, you guessed the word right! You may live!\n")
else:
    print("Sorry, you lost!\n")
