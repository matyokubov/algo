x,y = map(float, input().split())
if all([y<=1.5, x>=-2, x<=2, y>=1]) or all([y>=abs(x), y<=1]):
    print("yes")
else:
    print("no")
