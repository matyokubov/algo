x, y = map(float, input().split())
mx = x
if mx>y:
 mx = y
 mn = x
else:
 mx = x
 mn = y
 
print(f"{mn} {mx}")  
