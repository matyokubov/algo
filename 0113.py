n = int(input())
nums = map(int, input().split())
negatives = []
for i in nums:
    if i<0: negatives.append(i)
negatives_average = sum(negatives)/len(negatives)
print(f"{negatives_average:.2f}")
