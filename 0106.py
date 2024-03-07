n = int(input())
nums = list(map(int, input().split()))
res = sum(list(map(lambda n: n**2, nums)))
print(res)
