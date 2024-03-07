n,m = map(int, input().split())
matrix = []
for i in range(n): matrix.append(list(map(int, input().split())))
matrix = list(zip(*matrix))
k = int(input())
matrix.pop(k-1)
matrix = list(zip(*matrix))
for line in matrix: print(*line)
