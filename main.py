import array as arr
from functions import *

# import list from bank
infile = "wordleList.txt"
wordList = importList(infile)

# initialize wordle
wordle = initializeWord()

# take guess
guess = guessWord()

# get results of guess
wordleResults = getGuess()


