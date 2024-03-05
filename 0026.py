from math import *
a,x,y = input().split()
a = int(a)
x,y = map(float, (x,y))
w2 = sqrt(e**(x*y)-x*sin(a*x)-(x**2+2)/(abs(x)+5))+sqrt(log(x**2+2)+5)
print(f"{w2:.2f}")    
