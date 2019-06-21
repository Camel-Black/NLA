import sys
sys.path.insert(0,"./lib")
import config as func
import numpy as np


a = func.readFromText("A.txt")
a=np.asarray(a)
print(a)
# print(type(b))
(Q,R)= func.givens_rotation(a)

print((Q,R))
# a= np.array([[1 , 3 , 7],
#             [3 , 5 , 5]])
# (q,r) = np.shape(a)
# print(q,r)