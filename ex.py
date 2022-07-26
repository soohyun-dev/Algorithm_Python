from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M=map(int,input().split())
iceberg=[]
for i in range(N):
    iceberg.append(list(map(int,input().split())))

def bfs(x,y,cnt):
    dq=deque()
    dq.append([x,y])
    while dq:
        X,Y=dq.popleft()
        for i in range(4):
            mx=X+vertical[i]
            my=Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if visitied[X][Y]==False:
                    if iceberg[mx][my]!=0 and iceberg[X][Y]==0:
                        iceberg[mx][my]-=1
                        if iceberg[mx][my]==0:
                            visitied[mx][my]=True
                    elif iceberg[mx][my]==0:
                        dq.append([mx,my])
        visitied[X][Y]=True  
    return cnt+1
        
year=0
check=False
while True:
    cnt=0
    result=[]
    visitied=[[False]*M for _ in range(N)]
    year+=1
    for i in range(N):
        for j in range(M):
            if iceberg[i][j]==0 and visitied[i][j]==False:
                cnt=bfs(i,j,cnt)     
                for k in range(N):
                    print(iceberg[k])
                print()
    if cnt==1:
        check=True
        break
    if cnt==0:
        break

if check:
    print(year-1)
else:
    print(0)