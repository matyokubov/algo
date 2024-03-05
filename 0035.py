a,b,c = map(int, input().split())
if c<=b<=a: a,b,c=map(lambda x: x*2, (a,b,c))
else: a,b,c=map(lambda x: abs(x), (a,b,c))
print(a,b,c)  
