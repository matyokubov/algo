from math import *
x,y=map(float,input().split())
t11 = (x**2+1)/(x**2+(x*y+y**2)/(y**2+(y+x*y)/(abs(x*y)+5)))+1/(1+cos(x)+1/sin(x))
print(f"{t11:.2f}") 
