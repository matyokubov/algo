from math import *
a = int(input())
x,y,h = -pi/2,0,pi/19
while x<=pi:
    y+=(a**a)**(1/3)+x**2*cos(a*x)
    x+=h
print(f"{y:.2f}")
