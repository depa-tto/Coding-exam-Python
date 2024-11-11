# how to model wordle as an object oriented program

import sys
import csv
from random import choice
from datetime import datetime
from termcolor import colored

def dictSetup(): 
    with open("./dataset/en_unigram_freq.csv", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        records = list(reader)

    records.pop(0)
    en_words = [x[0] for x in records]
    return [x.upper() for x in en_words if len(x) == 5]

class Wordle: 
    # fields
    max_attempts = 6
    en_5_dict = []
    guess_history = []
    colored_history = []
    tile_history = []
    target = None
    
    tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}
    
    def __init__(self, attempts=None):
        # read and create the dictioanry
        if attempts is not None:
            self.max_attempts = attempts # so now the user can choose the number of attempts

        
        self.en_words_dict = dictSetup()

        # pick the target
        self.setTarget()
        self.printTarget()

    
    def setTarget(self):
        self.target = choice(self.en_5_dict)    


    def printTarget(self):
        print('the target word is ', self.target)
    
    
    
myWordleGame = Wordle()
# myLongWordleGame = Wordle(attempts=10)

