def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
	if char == aStr[(len(aStr)-1)/2]:
		return True
	elif char < aStr[(len(aStr)-1)/2]:
		return isIn(char, aStr[:(len(aStr)-1)/2])
	else:
		return isIn(char, aStr[(len(aStr)-1)/2]:)

char = float(raw_input('Enter char: '))
aStr = int(raw_input('Enter string: '))
print isIn(char, aStr)