from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0,1,1,-1,-1]
parallel=[0,0,1,-1,-1,1,-1,1]

N,M=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]
dq=deque()
for i in range(N):
    for j in range(M):
        if MAP[i][j]==1:
            dq.append([i,j])

def bfs():
    MAX=0
    while dq:
        X,Y=dq.popleft()
        for i in range(8):
            mx,my=X+vertical[i],Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==0:
                    dq.append([mx,my])
                    MAP[mx][my]=MAP[X][Y]+1
                    if MAX<MAP[mx][my]:
                        MAX=MAP[mx][my]
    return MAX-1

print(bfs())