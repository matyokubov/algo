x,y,z =  map(int, input().split())
if all([x+y>z, x+z>y, y+z>x]): print("YES")
else: print("NO")
