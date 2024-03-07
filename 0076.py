from math import *
a,b,c = map(int, input().split())
x,h,y = a,3,0
while x<=c:
    y += ((a*x+b)/(b**2+cos(x)**2))**(1/3)-(sin(x**2)/(a*b))
    x+=h
print(f"{y:.2f}")
