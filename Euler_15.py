def makegrid(row,col):
    return [[j for j in range(col)]for i in range(row)]
# print(makegrid(2,2))


x=[1,2,3]
y=['a','b','c']

x.append(y)
print(x)