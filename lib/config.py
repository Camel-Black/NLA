import numpy as np
from math import hypot,sqrt

def computation_given_entries(a, b):
    r = hypot(a, b) 
    c = a/r
    s = -b/r #sin = -b/sqrt(a,b)

    return (c, s)

def givens_rotation(A):
    
    (num_rows, num_cols) = np.shape(A)
    
    Q = np.identity(num_rows)
    R = np.copy(A)

    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)
    
    for (row, col) in zip(rows, cols): #
        if R[row, col] != 0:
            
            
            (c, s) = computation_given_entries(R[col, col], R[row, col])
            

            G = np.identity(num_rows)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s

            R = np.dot(G, R)
            Q = np.dot(Q, G.T)

    return Q, R

def readFromTextA(myFile):
    A=[]
    with open(myFile) as file:
        for line in file:
            a = list(filter(lambda x: x != '', [x for x in line.replace('\n', '').split(" ")]))
            A.append(list(map(lambda x : float(x), a)))
    return A	


def readFromTextB(myFile):
    b = []
    with open(myFile) as file:
        for line in file:
            b.append([float(x) for x in line.replace('\n', '').split(" ")])
    return b
def linearsolver(A,b):
  n = len(A)
  M = A

  i = 0
  for x in M:
   x.append(b[i])
   i += 1

  for k in range(n):
   for i in range(k,n):
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k]
     else:
        pass

   for j in range(k+1,n):
       q = float(M[j][k]) / M[k][k]
       for m in range(k, n+1):
          M[j][m] -=  q * M[k][m]

  x = [0 for i in range(n)]

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  print(x)
