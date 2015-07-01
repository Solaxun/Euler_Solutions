
import string
import itertools

def translate(word,numrange):
    a,b,c=numrange
    return word.replace('a',str(a)).replace('b',str(b)).replace('c',str(c))

pythagorean='a**2+b**2==c**2'
numrange=itertools.combinations(range(300),3)

for num in numrange:
    if(eval(translate(pythagorean,num))) and sum(num) == 1000:
        print (translate(pythagorean,num))

