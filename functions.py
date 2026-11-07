def importList(infile): # return array
    infile = open("wordleList.txt", "r")
    wordList = infile.read().splitlines()
    return wordList

def initializeWord(): # return array
    w = "white"
    wordle = ["w", "w", "w", "w", "w"]
    return wordle

def guessWord():
    guess = input("Enter your guess: ")

    return guess

def checkGuess():
    print("Enter the results of your first guess:")
    print("---------------------------------------")
    print("G for green")
    print("Y for yellow")
    print("W for white")
    print("---------------------------------------")

    initialWord = initializeWord()

    wordleGuess = 
    value 
    for i in (0,6):
        input(f"What was the result of letter {i + 1}? (g/y/w): ")



def wordleSolved(guess):
    return True

