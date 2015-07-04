import random
from collections import OrderedDict

def gamble(capital=1,f=0.25,flips=1000):
    for i in range(flips):
        flip=random.choice(['heads','tails'])
        bet=f*capital
        if flip=='heads':
            capital+=bet*2
        else:
            capital-=bet
    return capital

def smallrandom(start,stop,step):
    while start<stop:
        yield start
        start+=step

gambles = [OrderedDict([(f,gamble(capital=1,f=f,flips=1000)) for f in 
            smallrandom(0,1,0.01)]) for i in range(1000)]

for set_gambles in gambles:
    print(max(set_gambles.items(),key = lambda x:x[1]))




