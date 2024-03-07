n = int(input())
nums = list(map(int, input().split()))
t = []
for i in nums:
    if i%2==1: t.append(i)
print(f"{sum(t)/len(t)+0.00001:.2f}")
