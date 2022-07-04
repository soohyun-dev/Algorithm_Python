N=int(input())
check=[[0]*N for _ in range(N)]

start=N//2

cnt=1
x=0
y=start
while cnt<=N*N:
    if check[x][y]==0:
        check[x][y]=cnt
    else:
        x+=1
        check[x][y]=cnt
    if cnt%N==0:
        x+=1
    else:
        x-=1
        y+=1
        if y>N-1:
            y=0
    if x<0:
            x=N-1
    if x>N-1:
        x=0
    cnt+=1

for i in range(N):
    print(*check[i], end=' ')
    print()
    