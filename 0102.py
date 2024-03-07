n = int(input())
nums = list(map(int, input().split()))
a,b = map(int, input().split())
range_ab = list(range(a-1, b))
min_n = min(nums)
res = []
for i in enumerate(nums):
    if i[0] in range_ab:
        print(f"{i[1]/min_n+0.001:.1f}", end=" ")
    else:
        print(f"{i[1]:.1f}", end=" ")
