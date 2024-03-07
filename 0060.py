x,y = map(float, input().split())
if x<=0:
    if x>=2*y-2 and y<=(x+2)/2:
        print("yes")
    else:
        print("no")
if x>0:
    if x**2+y**2<=1:
        print("yes")
    else:
        print("no")
