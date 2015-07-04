x = 600851475143
# 

def eratosthenes(num):
    sieve=[True]*int(num)
    for i,val in enumerate(sieve):
        if i==2:
            sieve[::i]=[False for i in range(int(num/2))]
    return sieve


print(eratosthenes(20))




