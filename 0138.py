n = int(input())
matrix, d1, d2 = [], [], []
for i in range(n): matrix.append(list(map(int, input().split())))
for i in range(n): d1.append(matrix[i][i])
matrix = list(map(lambda line: list(reversed(line)), matrix))
for i in range(n): d2.append(matrix[i][i])
res = [max(d1), min(d2)]
print(*res)
