def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTuple = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            newTuple = newTuple + (aTup[i],)
    return newTuple
