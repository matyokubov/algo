from math import *
a,x,y=input().split()
a = int(a)
x,y = float(x), float(y)
TT = sqrt(y**2+e**x+sqrt(e**x+a/(x**2+2))+cos(x)**2/sin(x**2))+cos(x)**3
print(f"{TT:.2f}")    
