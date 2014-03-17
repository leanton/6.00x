# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#
def simulationWithDrug(numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, clearProb = 0.05, resistances = {'guttagonol': False, 'grimpex': False},
                       mutProb = 0.005, numTrials = 100):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    viruses = []
    avg = []
    avgres = []
    finalpop = []
    delay = 150
    delay2 = delay + 0
    LENGTH = delay2 + 150
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    for i in range(numTrials):
        pop = []
        popres = []
        pat = TreatedPatient(viruses, maxPop)   
        for t in range(LENGTH):
            pop.append(float(pat.update()))
            popres.append(float(pat.getResistPop(['guttagonol'])))
            if (t == delay):
                pat.addPrescription('guttagonol')
            if (t == delay2):
                pat.addPrescription('grimpex')
        finalpop.append(pop[-1])
        print('In progress: ' + str(i+1) + ' percent(s) complete')
        if i == 0:
            avg = pop
            avgres = popres
        else:
            for ind in range(LENGTH):
                avg[ind] = (avg[ind]*i + pop[ind])/float(i+1)
                avgres[ind] = (avgres[ind]*i + popres[ind])/float(i+1)
    #pylab.plot(range(LENGTH), avg, label = 'All Virus')
    #pylab.plot(range(LENGTH), avgres, label = 'ResistantVirus Population')
    #pylab.title('ResistantVirus simulation')
    #pylab.xlabel('Time Steps')
    #pylab.ylabel('Virus Population')
    #pylab.legend()
    #pylab.show()
    pylab.hist(finalpop, 10)
    pylab.show()

simulationWithDrug()


def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
