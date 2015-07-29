def collatz(num):
    nums=[num]
    while num>1:
        if num%2==0:
            num/=2
            nums.append(num)
        elif num%2!=0:
            num=num*3+1
            nums.append(num)
    return nums


x=[(len(collatz(i)),i) for i in range(1,1000001)]
print(max(x,key=lambda x:x[0]))
