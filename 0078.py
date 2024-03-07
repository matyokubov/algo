a,b,c = map(int, input().split())
x,y,h = a,0,2
while x<=b:
    y+=(a**b+b**x+c**a)/(2*x**2+3*a**x)
    x+=h
print(f"{y:.2f}")
