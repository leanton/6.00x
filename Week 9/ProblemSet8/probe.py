# Problem Set 8: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab
from ps8b_precompiled_27 import *  

''' 
Begin helper code
'''




def simulationWithoutDrug(numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, clearProb = 0.05,
                          numTrials = 10):
    LENGTH = 300
    avg = []
    viruses = []
    for v in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    for i in range(numTrials):
        pop = []
        pat = Patient(viruses, maxPop)
        for t in range(LENGTH):
            pop.append(float(pat.update()))
        if i == 0:
            avg = pop
        else:
            for ind in range(LENGTH):
                avg[ind] = (avg[ind]*i + pop[ind])/float(i+1)
    pylab.plot(range(LENGTH), avg, label = 'SimpleVirus')
    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend()
    pylab.show()

simulationWithoutDrug()



