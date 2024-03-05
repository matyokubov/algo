a,b,c,d = map(float, input().split())
mx = max(a,b,c,d)
mn = min(a,b,c,d)
if a<=b<=c<=d: a = b = c = d = mx
else: a = b = c = d = mn
print(f"{a:.2f} {b:.2f} {c:.2f} {d:.2f}")
