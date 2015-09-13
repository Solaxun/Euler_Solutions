import itertools
def get_proper_divisors(num):
    return [i for i in range(1,num) if num%i==0]

abundant=[]
for i in range(1,28123+1):
    if sum(get_proper_divisors(i))>i:
        abundant.append(i)

combs= set(x+y for x,y in itertools.product(abundant,repeat=2))
answer=set([num for num in range(1,28123+1)])
print(sum(answer-combs))
