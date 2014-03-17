def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    count = {}
    #count[1] = 'sad'
    #print aDict.items()
    for i in aDict.items():
    #	print i[0]
       count[len(i[1])] = i[0]
    #print count
    return count[max(count.keys())]


biggest({'a': [4, 14, 15, 6, 4, 18, 9, 19, 20], 'c': [], 'b': [12, 20, 15, 18, 9, 14]})
    
