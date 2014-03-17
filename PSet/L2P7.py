def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
    	return 0
    return 1 + lenRecur(aStr[:-1])




string = str(raw_input('Enter a string: '))
print lenRecur(string)