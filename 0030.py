from math import  *
x,y,z = map(float, input().split())
x = int(x)
AF = 2**(-x)*sqrt(x+(abs(y)+2)**0.25)*((e**(x-1)/sin(z+2))+2)**(1/3)
print(f"{AF:.2f}") 
