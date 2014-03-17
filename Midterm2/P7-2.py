import random
import pylab

def generateScores(numTrials):
    grade = []
    gradepass = []
    mid1 = range(50, 81)
    mid2 = range(60, 91)
    final = range(55, 96)
    for i in range(numTrials):
        pm1 = random.choice(mid1)
        pm2 = random.choice(mid2)
        pf = random.choice(final)
        grade.append(pm1 * 0.25 + pm2 * 0.25 + pf * 0.5)
    return grade

def plotQuizzes():
    data = generateScores(10000)
    pylab.figure()
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Scores')
    pylab.ylabel('Number of Trials')
    pylab.hist(data, 7)
    pylab.show()

plotQuizzes()