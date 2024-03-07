from math import *
a,x,y,h = int(input()),0,0,0.5
while x<=10:
    y += a*cos(x)-sin(x**2)
    x+=h
print(f"{y:.2f}")
