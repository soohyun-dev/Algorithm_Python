from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M,K=map(int,input().split())
MAP=[]
for i in range(N):
    MAP.append(list(map(int,input().rstrip())))

def bfs(x,y,skill):
    visited=[[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[x][y][skill]=1
    dq=deque()
    dq.append([x,y,skill])
    while dq:
        X,Y,Z=dq.popleft()
        if X==N-1 and Y==M-1:
            return visited[X][Y][Z]
        for i in range(4):
            mx=X+vertical[i]
            my=Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==1 and Z>0 and visited[mx][my][Z-1]==0:
                    visited[mx][my][Z-1]=visited[X][Y][Z]+1
                    dq.append([mx,my,Z-1])
                elif MAP[mx][my]==0 and visited[mx][my][Z]==0:
                    visited[mx][my][Z]=visited[X][Y][Z]+1
                    dq.append([mx,my,Z])                
                   
    return -1

print(bfs(0,0,K))