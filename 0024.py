from math import *
a,b,c,x = input().split()
a,b,c = map(int, [a,b,c])
x = float(x)
w1 = 0.75+(8.2*x**2+sqrt(abs(x**3+3*x)+cos(x-2)))/(a/4+b/3+c/2+1)
print(f"{w1:.2f}") 
