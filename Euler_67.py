
with open('c:/users/mwoodworth/downloads/euler_67.txt') as f:
	triangle=(f.read())
triangle= [list(map(int,row.split())) for row in triangle.split('\n') if row]
triangle=sorted(triangle,reverse=True,key=len)

while len(triangle)>=2:
	triangle[0:2]=[[max(triangle[0][j]+triangle[1][j],triangle[0][j+1]+triangle[1][j]) for j in range(len(triangle[1]))]]
print(*triangle[0])