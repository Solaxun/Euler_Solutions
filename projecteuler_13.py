f = open('numbers.txt','r')
numbers = f.readlines()

strippednumbers=[]
for i in numbers:
    strippednumbers.append(i.strip())

finalist=[]
for i in strippednumbers:
    finalist.append(int(i))

x= str(sum(finalist))
print x[0:10]+ '      >>>>>  this is the fucking answer, dude!'
print len(x[0:10])


