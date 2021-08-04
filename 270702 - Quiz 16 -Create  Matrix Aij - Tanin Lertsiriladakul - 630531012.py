"""
Created on Wed Aug  4 13:21:41 2021

@Auther : Tanin Lertsiriladakul 630531012
"""

#Quiz 16 : Creat a Matrix Aij
import numpy as np
N = int(input("Enter the number of row and collum"))
x = np.identity(N)
# Construct NxN matrix 
for i in range(N):
     for j in range(N):
        if i < j :
            x[i][j] = 0 
        elif i==j :
            x[i][j] = 1
        else:
            x[i][j] = -1
print(x)