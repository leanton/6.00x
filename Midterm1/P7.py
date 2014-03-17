def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    a = 0
    b = 0
    c = 0
    if n==6 or n==9 or n == 12 or n==18 or n == 15:
		return True


    for it_c in range(2*n/20):
    	if (b >0):
    		b-=1
    	if (a > 0):
    		a -=1
    	c = it_c
    	if (6*a + 9*b + 20*c == n):
    		return True
    	for it_b in range(2* n/9):
    		if (a > 0):
    			a -=1
    		b = it_b
    		if (6*a + 9*b + 20*c == n):
    			return True
    		for it_a in range(2* n/6):
    			
    			a = it_a
    			#print a, b, c
    			if (6*a + 9*b + 20*c == n):
    				return True

    return False

print McNuggets(0)
print McNuggets(6)
print McNuggets(9)
print McNuggets(20)
print McNuggets(26)
print McNuggets(35)
print McNuggets(31)
print McNuggets(2790)
