n,x = map(int, input().split())
k = 1
s = 0
for i in range(1, n+1):
    s += k*(1/x**(2*i))
    k = -k
print(f"{s:.3f}")
