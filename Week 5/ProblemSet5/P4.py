def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
    	return True
    elif len(word) == 0:
    	return False
    elif x[0] == word[0]:
    	return x_ian(x[1:], word[1:])
    else:
    	return x_ian(x, word[1:])

print x_ian('eric', 'algebraic')
print x_ian('john', 'mahjong')
print x_ian('alvin', 'palavering')
print x_ian('sarina', 'czarina')