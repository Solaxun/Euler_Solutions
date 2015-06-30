
notprime={}
primes={}


def isprime(num):
    if num %2==0 and num > 2:
        notprime[num]=True
        return False
    prime=True
    x = num-1
    while x>1:
        if notprime.get(num): return False
        if primes.get(num): return True
        if (num%x)==0:
            prime=False
            notprime[num]=True
            break
        x-=1
    if prime:primes[num]=True
    return prime



primes=[i for i in range(10000) if isprime(i)]
print(primes)
print(notprime)

