def stdDevOfLengths(L):
	if len(L) == 0:
		return float('nan')
	sdev = 0.0
	s = []
	for word in L:
		s.append(len(word))
	mean = sum(s)/len(s)
	for num in s:
		sdev += (num - mean)**2
	return (sdev/len(s))

print stdDevOfLengths(['a', 'z', 'p'])
print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
print stdDevOfLengths(['aaaaaaaaaa', 'aaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa', 'aaaaa'])