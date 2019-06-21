import sys
sys.path.insert(0,"./lib")
import config as func

A = func.readFromText("A.txt")
Q,R = func.householder(A)

print(Q)
print(A)
