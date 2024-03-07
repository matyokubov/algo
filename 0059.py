x,y = map(float, input().split())
if x<=(1-y)/2 and y>=2*x-1 and y>=x/-0.5-1 and (x+0.5)/0.5>=y:
    print("yes")
else:
    print("no")
