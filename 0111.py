n = int(input())
nums = list(map(int, input().split()))
m = int(input())
print(sum([i if i>m else 0 for i in nums]))
