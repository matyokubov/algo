n = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
res = list(map(lambda x: f"{x/max_num +0.00001:.2f}", nums))
print(*res)
