import numpy as np
from math import hypot,sqrt

def computation_given_entries(a, b):
    r = hypot(a, b) 
    c = a/r
    s = -b/r #sin = -b/sqrt(a,b)

    return (c, s)

def givens_rotation(A):
    
    (num_rows, num_cols) = np.shape(A)
    
    # Initialize orthogonal matrix Q and upper triangular matrix R.
    Q = np.identity(num_rows)
    R = np.copy(A)

    # Iterate over lower triangular matrix.
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)
    
    for (row, col) in zip(rows, cols): #
        if R[row, col] != 0:
            
            
            (c, s) = computation_given_entries(R[col, col], R[row, col])
            print(R[col, col], R[row, col])

            G = np.identity(num_rows)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s

            R = np.dot(G, R)
            Q = np.dot(Q, G.T)

    return (Q, R)

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
