import array as arr
from functions import Game

def main():
    # start counter 
    counter = 5
    # import list from bank
    infile = "wordleList.txt"
    wordList = Game.importList(infile)

    # initialize wordle
    wordle = Game.initializeWord()

    while counter > 0 and not Game.wordleSolved(wordle):
        # take guess
        wordleGuess = Game.guessWord()

        # get results of guess
        wordleGuess = Game.getGuess()

        # filter list based on guess
        wordList = Game.filterList(wordleGuess, wordList)

        # display list of possible words
        Game.displayList(wordList)

        # display current state of wordle
        Game.displayWordle(wordle)

        # display number of guesses left
        counter = Game.guessesLeft(counter)

        # display results
        Game.displayResults(wordleGuess)
        
        
    # display final results
    Game.finalResults(wordleGuess, wordList)

if __name__ == "__main__":
    main()