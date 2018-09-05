# This program will run the game hangman

# random module will be used to generate random word from words list

import random

# list of words to use in game
list_of_words = ["chicken", "apple", "juice", "carrot", "hangman", "program", "success", "hackbright"]

# display dashes for player to see how many letters are in the word to guess


print random.choice(list_of_words)


def greet_user():
    """greets user to hangman"""
    print "Welcome to Hangman!"

greet_user()

def player():
    """stores player's name"""
    name = input("What's your name? ")
    return name

player()
