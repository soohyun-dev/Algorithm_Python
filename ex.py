N=int(input())
arr=list(map(int,input().split()))
visited=[False]*(N+1)
k=2 # 직전 배터리 소모량
b=100  # 남은 배터리량
tmp=0
check=False
for i in range(N):
    t=arr[i]
    if not visited[t]:
        visited[tmp]=False
        tmp=t
        visited[t]=True
        b-=2
        k=2
    else:
        if check==True:
            k=1
            check=False
        k*=2
        b-=k
    if b<=0:
        b=100
        k=0
        check=True
print(100-b)