#imports
import random
import hangman_picture
from words import words

def select_word(words):
    return random.choice(words)

def print_hangman_word(hangman_word):
    print(" _ " * len(hangman_word))

def letter_input_correct(input, hangman_word):
    input = letter("Pick a letter - ")
    if len(input) > 1 or not guess.isalpha():
        print("You can only pick a single letter. Try again - ")
        sys.exit()
    else: 
        if input in hangman_word:
            return True
        else:
            return False
        print(used_guesses(input))

def used_guesses = input
  if used_guesses in input:
        print("You have already guessed that letter. Please pick another - ")

remaining_attempts = 6
guessed_letters = ""

print("Hangman Game")
hangman_word = select_word(words)
print(hangman_picture.get_hangman_picture(remaining_attempts))
print_hangman_word(hangman_word)

#needed for heroku set up
#print_title()
#while True:
 #   name = input("Please enter your name:\n")