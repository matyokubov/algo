from math import *
n = int(input())
k = 1
s = 0
for i in range(1, n+1):
    s += k*(1/factorial(2*i-1))
    k = -k
print(f"{s:.4f}")
