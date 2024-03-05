from math import *
a,x = input().split()
a = int(a); x = float(x)
TT = (sqrt(x-1)+sqrt(x+2)+log(sqrt(a*x**2)+2)/log(10))/(sqrt(sqrt(x+2)+sqrt(x+24)+x**5))
print(f"{TT:.2f}")
