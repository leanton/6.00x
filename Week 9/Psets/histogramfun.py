import pylab


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

VOWELS = 'aeiou'

def plotVowelProportionHistogram(wordList, numBins=30):
    vowelsList = []
    for word in wordList:
        numVowels = 0
        for letter in word.lower():
            if letter in VOWELS:
                numVowels = numVowels + 1
        vowelsList.append(numVowels/float(len(word)))
    pylab.figure()
    pylab.hist(vowelsList, numBins)
    pylab.show()
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
