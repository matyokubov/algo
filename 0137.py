n = int(input())
matrix, arr1 = [], []
for i in range(n): matrix.append(list(map(int, input().split())))
m = int(input())
for line in matrix:
    for item in line:
        if item%m==0: arr1.append(item)
res = sum(arr1)/len(arr1)
print(f"{res:.2f}")
