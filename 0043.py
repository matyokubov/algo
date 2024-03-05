x,y = map(float, input().split())
if all((x<0, y<0)): x,y=map(lambda n: abs(n), (x,y))
elif any((x<0, y<0)): x,y=map(lambda n: n+0.5, (x,y))
print(x,y) 
