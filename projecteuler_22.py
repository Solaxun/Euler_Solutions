
from string import ascii_lowercase
from time import *
start = time()
listvalues = {} #dictionary with alphabet letter:index

for x,i in enumerate(ascii_lowercase):
    listvalues[i.upper()]=x+1

f = open('names.txt','r')
names=f.read().replace('"',"")
namelist=names.split(',')
sortednames = sorted(namelist)

stuff = []
for i in sortednames:
    stuff.append([])

for index,name in enumerate(sortednames):
    for letter in name:
        stuff[index].append(listvalues.get(letter))

answer=[]
for index,lists in enumerate(stuff):
    answer.append(sum(lists)*(index+1))

print sum(answer)
end = time()
print end-start

{
	



	
}