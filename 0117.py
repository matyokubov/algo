n = int(input())
nums = list(map(int, input().split()))
t = nums[0::2]
res = sum(t)
print(res)
