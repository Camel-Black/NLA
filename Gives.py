import sys
sys.path.insert(0,"./lib")
import config as func



a = func.readFromText("A.txt")
(Q,R)= func.givens_rotation(a)

print((Q,R))
