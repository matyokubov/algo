from math import *
n,x = map(int, input().split())
s = 0
k = 1
for i in range(1, n+1):
    s += k*((x**(2*i-1))/(factorial(2*i-1)))
    k *= -1
print(f"{s:.3f}")
