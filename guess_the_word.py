# Courtney Garcia
# CIS256 Fall 2026
# Programming Assignment 4


import random

# Words the game can choose
words = ["running", "purple", "coffee", "medal", "training"]

# Pick a random word
secret_word = random.choice(words)

# Track guessed letters
guessed_letters = []

# 7 wrong gueeses allowed
attempts = 6

# Underscore the secret word
display_word = ["_"] * len(secret_word)

print("Welcome to Guess the Word!")
print(" ".join(display_word))

