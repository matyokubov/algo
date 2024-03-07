from math import *
n,x=map(int, input().split())
s,k=0,1
for i in range(1,n+1):
    s+=k*(x**(2*i-2))/factorial(2*i-2)
    k*=-1
print(f"{s:.3f}")
