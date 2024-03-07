n = int(input())
nums = list(map(int, input().split()))
res = [f"{i/min(nums):.2f}" for i in nums]
print(*res)
