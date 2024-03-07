n = int(input())
nums = list(map(int, input().split()))
average1 = sum(nums)/n
new_nums = []
for num in nums:
    if num<average1:
        new_nums.append(num)
average2 = sum(new_nums)/len(new_nums)
print(f"{average2:.2f}")
