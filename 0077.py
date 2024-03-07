from math import *
a,b,c,d = map(int, input().split())
x,h,y = c,2,0
while x<=d:
    y+=((sin(a*x)+b**(2*c))/(b**2+cos(x)**2))**(1/3) - (sin(x**2))/(a*b)
    x+=h
print(f"{y:.2f}")
