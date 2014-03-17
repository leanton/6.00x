import pylab

a = 3.0
b = 2.0
c = 1.0
accuracy = 0.001
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = pylab.array(yVals)
xVals = 2*pylab.array(xVals)
i = 1
r = pylab.polyfit(xVals, yVals, 1, full=True)[i][0]
print r, type(r)
while r > accuracy:
	i += 1
	r = pylab.polyfit(xVals, yVals, i, full=True)[1][0]
	s = pylab.polyfit(xVals, yVals, i, full=True)[0]
print i
print r
print s

def findOrder(xVals, yVals, accuracy = 1.0e-1):
    # Your Code Here
    i = 0
    r = pylab.polyfit(xVals, yVals, 0, full=True)[1][0]
    while r > accuracy:
        i += 1
        r = pylab.polyfit(xVals, yVals, i, full=True)[1][0]
    s = pylab.polyfit(xVals, yVals, i, full=True)[0]
    return s

print 'Checking task!'
print findOrder(xVals, yVals)