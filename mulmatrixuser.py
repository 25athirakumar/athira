R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
matrix = [] 
print("Enter the entries rowwise:") 
for i in range(R): 
    a =[] 
    for j in range(C):    
         a.append(int(input())) 
    matrix.append(a)  
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
	for i in range(len(X)):
       for j in range(len(Y[0])):
          for k in range(len(Y)):
			result[i][j] += X[i][k] * Y[k][j]  
for r in result:  
   print(r)  