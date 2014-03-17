from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    score = 0
    bestWord = ''
    #t0 = time.clock()
    for word in wordList:
        if isValidWord(word, hand, wordList):
            length = 0
            for letter in hand:
                length += hand.get(letter, 0)
            score_new = getWordScore(word, length)
            if (score_new > score):
                score = score_new
                bestWord = word
    if score != 0:
        return bestWord
    else:
        return None
    #print('end of search')
    #print time.clock() - t0, "seconds process time"



#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    # TO DO ... <-- Remove this comment when you code this function
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    hand = {}
    while True:
        command = raw_input('\nEnter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if command == 'e':
            break
        elif command == 'r' and len(hand) == 0:
            print('You have not played a hand yet. Please play a new hand first!')
        elif command == 'n':
            command_2 = raw_input('Choose person to play [u] - user, [c] - computer: ')
            hand = dealHand(HAND_SIZE)
            if command_2 == 'c':
                compPlayHand(hand.copy(), wordList)
            elif command_2 == 'u':
                playHand(hand.copy(), wordList, HAND_SIZE)
            else:
                print('Invalid command.\n')
        elif command == 'r' and len(hand) != 0:
            command_2 = raw_input('Choose person to play [u] - user, [c] - computer: ')
            if command_2 == 'c':
                compPlayHand(hand.copy(), wordList)
            elif command_2 == 'u':
                playHand(hand.copy(), wordList, HAND_SIZE)
            else:
                print('Invalid command.\n')
        else:
            print('Invalid command.\n')

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #playGame(wordList)
    compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList)


