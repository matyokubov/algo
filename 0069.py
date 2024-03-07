from math import *
n,x = map(int, input().split())
s = 0
k = -1
for i in range(1, n+1):
    s += k*((x**i)/(factorial(i)))
    k *= -1
print(f"{s:.3f}")
