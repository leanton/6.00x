import random

def test(numTrials):
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    # Your Code Here
    n = 100
    yes = 0
    for i in range(numTrials):
        africa = 0
        europe = 0
        samerica = 0
        asia = 0
        for i in range(n):
            rand = random.random()
            if rand < 0.25:
                africa += 1
            if rand < 0.5 and rand > 0.25:
                europe += 1
            if rand < 0.75 and rand > 0.5:
                samerica += 1
            if rand > 0.75:
                asia += 1
        #print africa, samerica, asia, europe
        if asia >= 30 or africa >= 30 or europe >= 30 or samerica >= 30:
            yes += 1
    prob = float(yes)/float(numTrials)
    return prob

print test(10000)