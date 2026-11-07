def importList():
    with open("wordleList.txt", "r") as file:
        wordList = file.read().splitlines()
