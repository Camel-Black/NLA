import sys
sys.path.insert(0,"./lib")

import config as func

a = func.readFromTextA("A.txt")
b = func.readFromTextB("b.txt")


x= func.maq(a,b)
print(x)