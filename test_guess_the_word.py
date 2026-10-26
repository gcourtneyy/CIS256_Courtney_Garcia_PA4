# Courtney Garcia
# CIS256 Fall 2026
# Programming Assignment 4


from guess_the_word import choose_word, check_guess, words

# Checks that the chosen word is in list
def test_choose_word():
    word = choose_word()
    assert word in words

# Test a correct letter
def test_correct_guess():
    assert check_guess("running", "r") == True

# Test incorecct letter
def test_wrong_guess():
    assert check_guess("running", "z") == False

