#imports
import random
from words import words

def select_word(words):
    return random.choice(words)

print(select_word(words))

remaining_attempts = 6
guessed letters = ""

#needed for heroku set up
#print_title()
#while True:
 #   name = input("Please enter your name:\n")