n = int(input())
nums = list(map(int, input().split()))
k,m = map(int, input().split())
x,y = [i if i==k or i==m else 1 for i in nums],1
for z in x: y*=z
print(y)
