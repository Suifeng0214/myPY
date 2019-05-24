p = [[0] * 30 for i in range(20)]
p[0][1] = 1

for i in range(1, (n+1) + 1 ):
	for j in range(1, (n+1) + 1 ):
		p[i][j] = p[i-1][j] + p[i-1][j-1]
		
for i in range(0, n+1):
	print( 2*(n-i) * ' ',end = "" )