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

# gambles = [OrderedDict([(f,gamble(capital=1,f=f,flips=1000)) for f in 
#             smallrandom(0.15,0.50,0.01)]) for i in range(1000)]
#             #narrowed range to 0.15-.50 through itering over the
#             #dicts this returned for min and max 
# ranges=[]
# for set_gambles in gambles:
#     ranges.append(max(set_gambles.items(),key = lambda x:x[1]))

# average=sum((x[0] for x in ranges))/len(ranges)
# print(average)

sim=[gamble(f=0.295) for i in range(1000)]
success=[capital for capital in sim if capital >=1e9]
print(len(success))

