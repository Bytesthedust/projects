from random import choice
# word list from charlesreid1 link: https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

def wordChoice():#opens word file and randomly choses a word
    wordFile = open("python\wordleClone\wordList")
    wordFileLines = wordFile.readlines()
    word = choice(wordFileLines)
    wordFile.close()
    return word.rstrip()

def checkGuess():#given the users guess, run through three possible scenarios
    return 0