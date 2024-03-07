n = int(input())
m1, m2, m3 = [], [], [[] for i in range(n)]
for i in range(n): m1.append(list(map(int, input().split())))
for i in range(n): m2.append(list(map(int, input().split())))
for i in range(n): m3[i] = m1[i] + m2[i]
for r in m3: print(*r)
