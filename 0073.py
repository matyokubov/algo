n_,x = map(int, input().split())
s = 0
for n in range(1, n_+1):
    s+=(x**(2*n-1))/(2*n-1)
print(f"{s:.3f}")
