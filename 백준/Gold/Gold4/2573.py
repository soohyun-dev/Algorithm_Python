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
    visited[x][y]=True
    while dq:
        X,Y=dq.popleft()
        for i in range(4):
            mx=X+vertical[i]
            my=Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if iceberg[mx][my]!=0 and visited[mx][my]==False:
                    dq.append([mx,my])
                    visited[mx][my]=True
                elif iceberg[mx][my]==0:
                    melting[X][Y]+=1
                    
    return cnt+1

year=0
while True:
    cnt=0
    visited=[[False]*M for _ in range(N)]
    melting=[[0 for _ in range(M)] for _ in range(N)] 
    for i in range(N):
        for j in range(M):
            if iceberg[i][j]!=0 and visited[i][j]==False:
                cnt=bfs(i,j,cnt)
                
    if cnt>=2:
        print(year)
        exit(0)
    if cnt==0:
        print(0)
        exit(0)
    
    for i in range(N):
        for j in range(M):
            iceberg[i][j]-=melting[i][j]
            if iceberg[i][j]<0:
                iceberg[i][j]=0
    year+=1
    