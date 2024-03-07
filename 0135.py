n,m = map(int, input().split())
matrix = []
for i in range(n): matrix.append(list(map(int, input().split())))
k = int(input())
matrix.pop(k-1)
for line in matrix: print(*line)
