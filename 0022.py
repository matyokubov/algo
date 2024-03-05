from math import *
x1,x2,c,d = input().split()
x1,x2 = map(float, [x1,x2])
c,d = map(int, [c,d])
f = abs(sin(c*x2**3+d*x1**3-c*d)**2/sqrt(c*x1**2+d*x2**2+7))+tan(x1*x2**2+d**3)
print(f"{f:.2f}")
