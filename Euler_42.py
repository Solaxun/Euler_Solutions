import os
os.chdir('C:/Users/MWoodworth/Downloads')

def is_triangle(num):
	i=1
	test=[]
	while sum(test)<=num:
		test.append(i)
		if num==sum(test):
			return True
		i+=1
	return False

alpha = '_abcdefghijklmnopqrstuvwxyz'
words = open('Euler_42.txt').read().replace('"','').lower().split(',')

wordvalues=sum(map(is_triangle,[sum([alpha.index(letter) for letter in word]) for word in words]))
print(wordvalues)