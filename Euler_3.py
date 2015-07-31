def isprime(num):
    prime=True
    init_divisor=num-1
    while init_divisor>1:
        if num%init_divisor == 0:
            prime=False
            break
        init_divisor-=1
    return num if prime else False

def prime_factors(num):
    factors=[]
    num=num
    while num>1:
        for i in range(2,int(num+1)):
            if num%i==0:
                factors.append(i)
                num/=i
                break
    return max(map(isprime,factors))

print(prime_factors(600851475143))