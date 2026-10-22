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

# 6 wrong guesses allowed
attempts = 6

# Underscore the secret word
display_word = ["_"] * len(secret_word)

print("Welcome to Guess the Word!")
print(" ".join(display_word))


# Keep playing until word is guessed or attempts run out
while attempts > 0 and "_" in display_word:
    guess = input("Guess a letter: ").lower()

    # Only one letter guessed at a time
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue
    
    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("Good guess!")

        # Show where letter belongs
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
            
    else:
        print("Wrong guess!")
        attempts -= 1

    print("Attempts left:", attempts)
    print(" ".join(display_word))

# Show final result
if "_" not in display_word:
    print("Good job! The word was", secret_word)
else:
    print("Game over! The word was", secret_word)




