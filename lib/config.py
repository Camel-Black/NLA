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
    #------------------------------#
def maq(A,b):
  n = len(A)
  M = A

  i = 0
  for x in M:
   x.append(b[i][0])
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
  return x


def LUP(A,b):
    n = len(A)
    A, b = np.asarray(A,dtype=np.float64),np.asarray(b,dtype=np.float64)
    L = np.asarray(np.identity(n))
    U = np.copy(A)
    P = np.identity(n)

    permutation = abs(U[:,0]).argsort()[::-1]
    print(permutation)
    U=U[permutation]
    P=P[permutation]

    for k in range(n):                          #for each column of A in Ab

        #Forward Elimination - Subtracting rows
        for j in range(k+1,n):                      #for each row under the diagonal of the kth column
            q = float(U[j][k]) / U[k][k]              #calculate the ratio to the value in the main diagonal

            L[j][k] = q

            for m in range(k, n):                     #for each each column in a Row j
                # Ab[j][m] -=  q * Ab[k][m]                   #calculate Rj - q*Rk.  This will result in all zeros under the main diagonal
                if m<len(U):
                    U[j][m] -= q * U[k][m]
    x = np.zeros(n)

    U = np.triu(U)
    return (np.asmatrix(L), np.asmatrix(U),np.asmatrix(P))