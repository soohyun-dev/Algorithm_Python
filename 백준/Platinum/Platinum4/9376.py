from collections import deque
from re import L
import sys

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

def bfs(x,y):
    dq=deque()
    dq.append([x,y])
    visited=[[-1]*(M+2) for _ in range(N+2)]
    visited[x][y]=0
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            mx=x+vertical[i]
            my=y+parallel[i]
            if 0<=mx<N+2 and 0<=my<M+2:
                if visited[mx][my]==-1:
                    if jail[mx][my]=='#':
                        visited[mx][my]=visited[x][y]+1
                        dq.append([mx,my])
                    elif jail[mx][my]=='.' or jail[mx][my]=='$':
                        visited[mx][my]=visited[x][y]
                        dq.appendleft([mx,my])
    return visited

for _ in range(int(input())):
    N,M=map(int,input().split())
    jail=['.'*(M+2)]
    for i in range(N):
        jail.append('.'+input().strip()+'.')
    jail.append('.'*(M+2))
    pri=[]
    for i in range(N+2):  #죄수 위치 파악
        for j in range(M+2):
            if jail[i][j]=='$':
                pri.append([i,j])
                
    first=bfs(pri[0][0],pri[0][1])
    second=bfs(pri[1][0],pri[1][1])
    out=bfs(0,0)
    answer=sys.maxsize
    
    for i in range(N+2):
        for j in range(M+2):
            if first[i][j]!=-1 and second[i][j]!=-1 and out[i][j]!=-1:
                tmp=first[i][j]+second[i][j]+out[i][j]
                if jail[i][j]=='*':
                    continue
                if jail[i][j]=='#':
                    tmp-=2
                answer=min(answer,tmp)
    print(answer)