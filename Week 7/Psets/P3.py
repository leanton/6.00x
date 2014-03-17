import pylab
import string

def loadData():
	inFile = open('julyTemps.txt', 'r', 0)
	line = inFile.readline()
	data = []
	#dataX = []
	dataY = []
	for line in inFile:
		data = string.split(line)
		if len(data) == 3 and data[0] != 'Day':
			#dataX.append(int(data[0]))
			dataY.append(int(data[1]))
	return dataY

		
dataY = loadData()
Y = []
for i in range(len(dataY)-1):
	Y.append(dataY[i+1] - dataY[i])
pylab.figure(1)
X = range(len(Y))
pylab.plot(Y)
pylab.show()
