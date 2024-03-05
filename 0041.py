x,y,z = map(float, input().split())
minn = min(x,y,z)
if all([x<1, y<1, z<1]):
    if minn==x:
        x = (y+z)/2
    elif minn==y:
        y = (x+z)/2
    else:
        z = (x+y)/2
print(x,y,z)
