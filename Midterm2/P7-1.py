import random

def sampleQuizzes():
    grade = []
    gradepass = []
    mid1 = range(50, 81)
    mid2 = range(60, 91)
    final = range(55, 96)
    for i in range(10000):
        pm1 = random.choice(mid1)
        pm2 = random.choice(mid2)
        pf = random.choice(final)
        grade.append(pm1 * 0.25 + pm2 * 0.25 + pf * 0.5)
    for num in grade:
    	if num >= 70.0 and num <= 75.0:
    		gradepass.append(num)
    prob = float(len(gradepass))/len(grade)
    return prob


print sampleQuizzes()
