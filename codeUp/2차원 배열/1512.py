N=int(input())
X,Y=map(int,input().split())
check=[[0]*N for _ in range(N)]
cnt=1
check[X-1][Y-1]=cnt

for i in range(Y-1,-1,-1):
    if check[X-1][i]==0:
        check[X-1][i]=check[X-1][i+1]+1
    cnt=check[X-1][i]
    for j in range(X-2,-1,-1):
        cnt+=1
        check[j][i]=cnt
    cnt=check[X-1][i]
    for j in range(X,N):
        cnt+=1
        check[j][i]=cnt
    
for i in range(Y,N):
    if check[X-1][i]==0:
        check[X-1][i]=check[X-1][i-1]+1
    cnt=check[X-1][i]
    for j in range(X-2,-1,-1):
        cnt+=1
        check[j][i]=cnt
    cnt=check[X-1][i]
    for j in range(X,N):
        cnt+=1
        check[j][i]=cnt
        
for i in range(N):
    print(*check[i], end=' ')
    print()