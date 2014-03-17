import random

def probTest(limit):
    n = 1
    prob = 1.0 / 6
    while (limit <= prob):
    	prob *= 5.0/6
    	n+=1
    return n

