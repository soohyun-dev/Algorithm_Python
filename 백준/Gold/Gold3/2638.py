from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M=map(int,input().split())
MAP=[]
for i in range(N):
    MAP.append(list(map(int,input().split())))


def bfs(x,y):
    visited=[[0 for _ in range(M)] for _ in range(N)]
    dq=deque()
    dq.append([x,y])
    while dq:
        X,Y=dq.popleft()
        visited[X][Y]=1
        for i in range(4):
            mx,my=X+vertical[i],Y+parallel[i]
            if 0<=mx<N and 0<=my<M and MAP[X][Y]==0:
                if MAP[mx][my]==1:
                    if visited[mx][my]==0:
                        visited[mx][my]+=1
                    elif visited[mx][my]==1:
                        visited[mx][my]=2
                        MAP[mx][my]=0
                elif MAP[mx][my]==0 and visited[mx][my]==0:
                    dq.append([mx,my])
                    visited[mx][my]=1
    cnt=0
    for i in range(N):
        for j in range(M):
            if MAP[i][j]!=0:
                cnt+=1
    return cnt

time=0
while True:
    result=bfs(0,0)
    time+=1
    if result==0:
        print(time)
        break