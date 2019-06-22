import sys
sys.path.insert(0,"./lib")
import config as func
import numpy as np


a = func.readFromTextA("A.txt")
a=np.asarray(a)

Q,R= func.givens_rotation(a)


b = func.readFromTextB("b.txt")

b = np.asarray(b)
p = np.dot(Q.T, b)
print("x : \n")
print(np.dot(np.linalg.inv(R), p))
