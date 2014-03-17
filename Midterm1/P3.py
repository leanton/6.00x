def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    a = 0
    while (b ** a <= x):
    	a += 1
    return a-1

print myLog(16, 2)
print myLog(15, 3)