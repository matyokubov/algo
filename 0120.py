n = int(input())
nums = list(map(int, input().split()))
x,y = map(int, input().split())
a,res = 0,0
for i in nums:
    if x<=i and i<=y: a+=1
res = len(nums)-a
print(res)
