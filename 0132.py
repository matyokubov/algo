L = int(input())
arr = list(map(int, input().split()))
n,m = map(int, input().split())
size_of_matrix = n*m
if size_of_matrix > L: arr+=[0 for i in range(size_of_matrix-L)]
elif size_of_matrix < L: arr = arr[L-size_of_matrix:]
matrix = []
for tm in range(0, n*m, m):
    matrix.append(arr[tm:tm+m])

for line in matrix: print(*line)
