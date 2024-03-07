from math import *
n_,k=map(int, input().split())
s,z=0,1
for n in range(0, n_+1):
    s+=z*k**n/factorial(n)
    z=-z
print(f"{s:.3f}")
