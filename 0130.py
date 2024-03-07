n, m = map(int, input().split())
min_vals, max_vals, vectors = [],[],[]
for i in range(n):
    matrix_line = list(map(int, input().split()))
    min_vals.append(min(matrix_line))
    max_vals.append(max(matrix_line))
    vectors.append(sum(matrix_line))
res = [min(min_vals), max(max_vals), vectors]
print(*vectors)
print(res[1],res[0])
