from math import *
n = int(input())
nums = list(map(int, input().split()))
r = [i if i%2==0 or i%5==0 else 1 for i in nums]
x = 1
for k in r: x*=k
res = sin(x)
print(f"{res:.2f}")
