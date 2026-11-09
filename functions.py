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
        for i in range(5):
            value = input(f"What was the result of letter {i + 1}? (g/y/w): ")
            wordleGuess.append(value.strip().lower())

        return wordleGuess

    def filterList(guess, wordleGuess, wordList) -> arr:
        guess = guess.strip().lower()
        colors = [c.strip().lower() for c in wordleGuess]

        for i in range(len(guess)):
            letter = guess[i]
            color = colors[i]
            if color == "g":
                wordList = [word for word in wordList if word[i] == letter]
            elif color == "y":
                wordList = [word for word in wordList if letter in word and word[i] != letter]
            elif color == "w":
                elsewhere = any(guess[j] == letter and colors[j] in ("g", "y") for j in range(len(guess)))
                if elsewhere:
                    wordList = [word for word in wordList if word[i] != letter]
                else:
                    wordList = [word for word in wordList if letter not in word]

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

    def finalResults(wordleGuess, wordList, counter) -> None:
        if Game.wordleSolved(wordleGuess):
            print(f"Congratulations! You solved the wordle in {counter + 1} guesses!")
        else:
            print("Sorry, you did not solve the wordle.")
            print("The possible words were:")
            Game.displayList(wordList)

