X=[[15,14,16],
	[13,16,19],
	[11,15,17]]
Y=[[2,4,6],
	[3,6,9],
	[1,5,7]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] - Y[i][j]
for r in result:
   print(r)
	