import random

def genEven():
	data = []
	for x in range(100):
		if x%2 == 0:
			data.append(x)
	return random.choice(data)

print genEven()