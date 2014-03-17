def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    s3 = ''
    if (len(s1) >= len(s2)):
    	smax = s1
    	length_min = len(s2)
    else:
    	smax = s2
    	length_min = len(s1)
    for i in range(length_min):
    	s3 += s1[i]
    	s3 += s2[i]
    s3 += smax[length_min:]
    return s3

print laceStrings('abcd', 'efghi')