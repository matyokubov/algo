from math import *
a,x = input().split()
a = int(a); x = float(x)
bb1 = x*sin(x/2+x/3+x/4)+(log(x**2-2)/log(10)+3**a)/(cos(x+3)*sin(x+3)+8)
print(f"{bb1:.2f}")  
