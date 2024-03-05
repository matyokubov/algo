x,y,z = map(float, input().split())
a = x+y+z
b = x+y/2
maxn = a
minn = b
if maxn<x:maxn=x
if maxn<y:maxn=y
if maxn<z:maxn=z
# =================
if minn>x:minn=x
if minn>y:minn=y
if minn>z:minn=z

print(f"{maxn:.2f} {minn**2:.2f}")  
