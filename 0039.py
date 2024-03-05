x,y = map(int, input().split())
a,b=x,y
if x<y:
    y=2*a*2*b
    x=(a+b)/2
else:
    x=2*a*2*b
    y=(a+b)/2
print(f"{x:.1f} {y:.1f}")  
