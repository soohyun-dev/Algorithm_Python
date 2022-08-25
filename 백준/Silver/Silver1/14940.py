from collections import deque
import sys
input=sys.stdin.readline

dr=[(0,1),(1,0),(-1,0),(0,-1)]

def bfs(start,MAP):
    MAP[start[0]][start[1]]=0
    dq=deque()
    dq.append(start)
    visited=[[False for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]]=True
    while dq:
        X,Y=dq.popleft()
        for i,j in dr:
            mx,my=X+i,Y+j
            if 0<=mx<N and 0<=my<M:
                if not visited[mx][my] and MAP[mx][my]==1:
                    visited[mx][my]=True
                    MAP[mx][my]=MAP[X][Y]+1
                    dq.append([mx,my])
                    
    for i in range(N):
        for j in range(M):
            if visited[i][j]==False and MAP[i][j]!=0:
                MAP[i][j]=-1
    return MAP
N,M=map(int,input().split())
MAP=[]
start=[]
for i in range(N):
    MAP.append(list(map(int,input().split())))
    for j in range(M):
        if MAP[i][j]==2:
            start=[i,j]

result=bfs(start,MAP)

for i in range(N):
    print(*MAP[i])