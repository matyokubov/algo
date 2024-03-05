arr = list(map(int, input().split()))
for n in enumerate(arr):
    val = n[1]
    idx = n[0]
    if val>0:
        arr[idx]=val**2
print(*arr)   
