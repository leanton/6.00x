import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    def getBall(listofBalls):
    	return random.choice(listofBalls)

    yes = 0
    for i in range(numTrials):
	    r1 = getBall(['red', 'red', 'red', 'blue', 'blue', 'blue'])
	    r2 = getBall(['red', 'red', 'blue', 'blue', 'blue'])
	    r3 = getBall(['red', 'blue', 'blue', 'blue'])
	    b1 = getBall(['red', 'red', 'red', 'blue', 'blue', 'blue'])
	    b2 = getBall(['red', 'red', 'red', 'blue', 'blue'])
	    b3 = getBall(['red', 'red', 'red', 'blue'])
	    #print r1, r2, r3

	    if (r1 == 'red' and r2 == 'red' and r3 == 'red') or (b1 == 'blue' and b2 == 'blue' and b3 == 'blue'):
	    	yes += 1

    return float(yes)/numTrials

print noReplacementSimulation(10000)

