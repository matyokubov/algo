a,b,c = map(int, input().split())
d = b**2-4*a*c
if d >= 0:
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)
    print(f"{x1:.2f} {x2:.2f}")
else: print('NO')    
