def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    length = 0
    for letter in hand:
        length += hand.get(letter, 0)
    return length

print calculateHandlen({'a': 1, 'b': 1})
print calculateHandlen({'a': 1, 'c': 0, 'b': 1})