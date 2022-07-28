from collections import deque
import copy

vertical=[0,-0,1,-1]
parallel=[1,-1,0,0]
N,M=map(int,input().split())
MAP=[]
for i in range(N):
    MAP.append(list(map(int,input())))
MAP[0][0]=-1
visited=[[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1
result=[]

def bfs(x,y,z):
    dq=deque()
    dq.append([0,0,0])
    while dq:
        x,y,z=dq.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][z]
        for i in range(4):
            mx=x+vertical[i]
            my=y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==1 and z==0:
                    visited[mx][my][1]=visited[x][y][0]+1
                    dq.append([mx,my,1])
                elif MAP[mx][my]==0 and visited[mx][my][z]==0:
                    visited[mx][my][z]=visited[x][y][z]+1
                    dq.append([mx,my,z])
    return -1

print(bfs(0,0,0))
