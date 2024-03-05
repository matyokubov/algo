x, y, z = map(float, input().split())
mx = x
mn = x
#========================
if mx<y:
    mx=y
if mx<z:
    mx=z
# =======================
if mn>y:
    mn=y
if mn>z:
    mn=z
#========================
print(f"{mx} {mn}")   
