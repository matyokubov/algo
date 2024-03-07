x,y = map(float, input().split())
if y<=0:
    if all([x>=(y-3)/2, y>=(x-1)/3]):
        print("yes")
    else:
        print("no")
elif y>0:
    if all([x>=(y-3)/2, y<=(-x)]):
        print("yes")
    else:
        print("no")
else:
    print("no")
