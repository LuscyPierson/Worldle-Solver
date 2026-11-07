import array as arr

def importList(infile) -> arr:
    infile = open("wordleList.txt", "r")
    wordList = infile.read().splitlines()
    return wordList

def initializeWord() -> arr:
    w = "white"
    wordle = ["w", "w", "w", "w", "w"]
    return wordle

def guessWord() -> str:
    guess = input("Enter your guess: ")

    return guess

def getGuess() -> str:
    print("Enter the results of your first guess:")
    print("---------------------------------------")
    print("G for green")
    print("Y for yellow")
    print("W for white")
    print("---------------------------------------")

    wordleGuess = [] 
    for i in (0,6):
        value = input(f"What was the result of letter {i + 1}? (g/y/w): ")
        wordleGuess.append(value)

    return wordleGuess

def filterList(wordleGuess, wordList) -> arr:
    for i in range(0, 5):
        if wordleGuess[i] == "g":
            wordList = [word for word in wordList if word[i] == wordleGuess[i]]
        elif wordleGuess[i] == "y":
            wordList = [word for word in wordList if wordleGuess[i] in word and word[i] != wordleGuess[i]]
        elif wordleGuess[i] == "w":
            wordList = [word for word in wordList if wordleGuess[i] not in word]

    return wordList
    



def wordleSolved(wordleGuess) -> bool:
    return True

