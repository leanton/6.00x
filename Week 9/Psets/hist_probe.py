import pylab as P
import random

data = []
for i in range(100):
	num = random.triangular(0, 100, 50)
	data.append(num)

P.hist(data, bins = 10)
P.show()
