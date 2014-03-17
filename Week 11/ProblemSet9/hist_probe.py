import pylab as P
import random

data = []
for i in range(10000):
	num = random.triangular(0, 100, 50)
	data.append(num)

P.hist(data, 100)
P.show()
