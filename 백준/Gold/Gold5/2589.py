from collections import deque
from copy import deepcopy

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M=map(int,input().split())
MAP=[]
for i in range(N):
    MAP.append(list(input()))
MAX=0
LAND=[]
for i in range(N):
    for j in range(M):
        if MAP[i][j]=='L':
            cnt=0
            for k in range(4):
                mx=i+vertical[k]
                my=j+parallel[k]
                if 0<=mx<N and 0<=my<M:
                    if MAP[mx][my]=='L':
                        cnt+=1
            if cnt<=2:
                LAND.append([i,j])

def bfs(x,y):
    COPY=deepcopy(MAP)
    COPY[x][y]='N'
    dq=deque()
    dq.append([x,y,0])
    tmp=0
    while dq:
        X,Y,cnt=dq.popleft()
        for i in range(4):
            mx=X+vertical[i]
            my=Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if COPY[mx][my]=='L':
                    COPY[mx][my]='N'
                    dq.append([mx,my,cnt+1])
                    tmp=cnt+1      
    return tmp

for i in LAND:
    x,y=i[0],i[1]
    result=bfs(x,y)
    if MAX<result:
        MAX=result

print(MAX)