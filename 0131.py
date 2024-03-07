n,m = map(int, input().split())
matrix, rotated_matrix = [],[[] for i in range(m)]
for i in range(n): matrix.append(list(map(int, input().split())))

vectors,min_vals,max_vals = [],[],[]
for line in matrix:
    min_vals.append(min(line))
    max_vals.append(max(line))
    for idx,item in enumerate(line):
        rotated_matrix[idx].append(item)
for line in rotated_matrix: vectors.append(sum(line))
print(*vectors)
print(max(max_vals),min(min_vals))
