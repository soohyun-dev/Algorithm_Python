N=int(input())
N_list=list(map(int,input().split()))

N_max=max(N_list)
check=[False]*(N_max+1)
for i in range(N):
    check[N_list[i]]=True

M=int(input())
M_list=list(map(int,input().split()))
result=[]

for i in range(M):
    if check[M_list[i]]==True:
        result.append(1)
    else:
        result.append(0)

print(*result)