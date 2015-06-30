stuff = []
answer=[]
for x in xrange (100,999):
    for y in xrange(100,999):
        product=x*y
        stuff.append(product)
    for i in stuff:
        if str(i)[::-1] == str(i):
            answer.append(int(str(i)))

print max(answer)



