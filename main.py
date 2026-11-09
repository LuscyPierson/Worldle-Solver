import array as arr
from functions import *

def main():
    # import list from bank
    infile = "wordleList.txt"
    wordList = importList(infile)

    # initialize wordle
    wordle = initializeWord()

    # take guess
    guess = guessWord()

    # get results of guess
    wordleGuess = getGuess()

    # filter list based on guess
    wordList = filterList(wordleGuess, wordList)