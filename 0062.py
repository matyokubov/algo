from math import *
n,k,s = int(input()),1,0
for i in range(1, n+1):
    s += k*(sin(i**i)/2**i)
    k = -k
print(f"{s:.2f}")  
