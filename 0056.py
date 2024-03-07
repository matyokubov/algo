x,y = map(float, input().split())
if all([x**2>=0.25-y**2,x**2<=1-y**2]):
    print("yes")
else:
    print("no")
