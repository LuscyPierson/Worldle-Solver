import array as arr

class Game:
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
        print("-----------------------------")
        print("G for green")
        print("Y for yellow")
        print("W for white")
        print("-----------------------------")

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

    def displayList(wordList) -> None:
        print("There are " + str(len(wordList)) + " possible words.")
        print("Here are the possible words:")
        print("-----------------------------")
        for word in wordList:
            print(word)
        print("-----------------------------")

    def displayWordle(wordle) -> None:
        print("The current state of the wordle is:")
        print("-----------------------------")
        print(wordle)
        print("-----------------------------")

    def guessesLeft(counter) -> int:
        counter -=1
        print("You have " + str(counter) + " guesses left.")
        print("-----------------------------")

        return counter


    def wordleSolved(wordleGuess) -> bool:
        result = False
        if wordleGuess == ["g", "g", "g", "g", "g"]:
            return True
        return result

    def stopGame(counter, wordleGuess) -> bool:
        result = False
        
        if counter == 0:
            result = True
        elif Game.wordleSolved(wordleGuess):
            result = True
        return result

    def displayResults(wordleGuess) -> None:
        print("The results of your guess are:")
        print("-----------------------------")
        print(wordleGuess)
        print("-----------------------------")

    def finalResults(wordleGuess, wordList) -> None:
        if Game.wordleSolved(wordleGuess):
            print("Congratulations! You solved the wordle!")
        else:
            print("Sorry, you did not solve the wordle.")
            print("The possible words were:")
            Game.displayList(wordList)

