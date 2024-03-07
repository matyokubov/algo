x,y = map(float, input().split())
if all([y>=0, x**2>=1-y**2,x**2<=4-y**2]):
    print("yes")
else:
    print("no")
