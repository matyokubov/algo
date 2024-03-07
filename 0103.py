n = int(input())
nums = list(map(int, input().split()))
k,l = map(int, input().split())
sliced_nums = nums[k-1:l]
average = sum(sliced_nums)/len(sliced_nums)
print(f"{average:.1f}")
