n = int(input())
arr = list(map(int,input().split()))
t,res_t = [i for i in arr[0:n:2]],1
for t_n in t: res_t*=t_n
res_j = sum([i for i in arr[1:n:2]])
print(f"{res_t/res_j:.2f}")
