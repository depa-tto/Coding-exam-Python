# we want to implement the Wordle game
# https://www.nytimes.com/games/wordle/index.html

# you have X attempts to guess the target word that is randomly selected within the 5-letter words in English

# rules:
## A correct letter turns green
## A correct letter in the wrong place turns yellow
## An incorrect letter turns gray

# for any attempt, the feedback must report green-yellow-gray letters
# use tiles to provide a feedback (see the pic in the attachment)


# cases to handle (with a message to the player)
# words that are not in the dictionary
# words with length different from 5
# words already guessed (do not consume tries, we need a history)

import csv
import random
from termcolor import colored  # type: ignore

# load the EN dictionary and isolate the 5 length words

with open("unigram_freq.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    records = list(reader)

records.pop(0)

# drop the frequencies
# [f(x) for x in itera

en_words = [x[0] for x in records]

# limit to 5 letter-words and switch to uppercase
# [f(x) for x in iterable if condition]

en_word_5 = []
for i in en_words:
    if len(i) == 5:
        en_word_5.append(i.upper())

# alternatively

en_word_5_second = [x.upper() for x in en_words if len(x) == 5]


# pick-up the target
# more sophisticated methods for choosing the target are possible
# consider random.choices that allows to consider weights associated with words
# the word frequencies could be used to make more probable the words that are less frequent
# this way, it is possible to define the game difficulty

target = random.choice(en_word_5)


max_attempts = 6
tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}


def check_guess(guess, target):
    global tiles  # i define the tiles object that is defined outside the body of the function. i am importing the variable
    colored_letters = []
    colored_tiles = []

    for i, letter in enumerate(guess):
        if guess[i] == target[i]:
            # color in green
            colored_letters.append(colored(guess[i], 'green'))
            colored_tiles.append(tiles["correct_place"])

        elif guess[i] in target:
            colored_letters.append(colored(guess[i], 'yellow'))
            colored_tiles.append(tiles["correct_letter"])

        else:
            colored_letters.append(guess[i])
            colored_tiles.append(tiles["incorrect"])
        
        print(colored_letters)
        print(colored_tiles)

        return "".join(colored_letters), "".join(
            colored_tiles
        )  # i am rebuilding the string one with letters and the other one with tiles


print("Welcome to WORDLE!")
print(f"Guess the target word, you have {max_attempts} tries.")
print(target)

history = []
colored_letters = []
colored_tiles = []
attempt = 1

# while loop consider the number of attemps that need to be lower than the maximum
while attempt <= max_attempts:
    # enter the guess
    guess = input("enter a 5-letters word: ").upper()
    if guess == target:
        print("the target is guessed")
        attempt = max_attempts + 1

    # check possible errors in the attempt:
    # not in dict, not 5 letters, consider history
    if len(guess) != 5:
        print("please enter a 5-letter word")
        # continue --> with continue i go back to revaluate the while condition, so i re-executing the loop
    elif not guess.isalpha():
        print("please enter a 5-letter word")
    elif guess in history:
        print("the guess is already tried, guess another one")
    elif guess in en_word_5:
        print("please, insert a word in the english dictonary")
    else:
        # if the guess is the target or provide a feedback
        history.append(guess)
        c_letters, c_tiles = check_guess(guess, target)

        colored_letters.append(c_letters)
        colored_tiles.append(c_tiles)

        print(colored)
        print(tiles)
        
        colored_letters.append(colored)
        colored_tiles.append(tiles)

        # increase the counter
        attempt += 1
