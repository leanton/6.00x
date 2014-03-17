def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
    	min_value = b
    	max_value = a
    else:
    	min_value = a
    	max_value = b
    while (max_value % min_value !=0):
    	min_value  = max_value % min_value
    return min_value

a = int(raw_input('Enter a: '))
b = int(raw_input('Enter b: '))
print gcdIter(a,b)