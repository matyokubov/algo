from math import *
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
x,y = [i if i>m else 1 for i in nums],1
for z in x: y*=z
res = log(y)
print(f"{res:.2f}")
