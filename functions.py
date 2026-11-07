def importList(infile):
    infile = open("wordleList.txt", "r")
    wordList = infile.read().splitlines()
    return wordList

def guessWord():
    guess = input("Enter your guess: ")

    return guess

