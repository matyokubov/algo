from math import *
x,y=map(float,input().split())
f1 = (2*tan(x+pi/6))/(1/3+cos(y+x**2)**2)+log2(x**2+2)
print(f"{f1:.2f}") 
