from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0,1,1,-1,-1]
parallel=[0,0,1,-1,-1,1,-1,1]

N,M=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]

def bfs(x,y):
    dq=deque()
    dq.append([x,y])
    MAP[x][y]=0
    while dq:
        X,Y=dq.popleft()
        for i in range(8):
            mx, my=X+vertical[i], Y+parallel[i]
            if  0<=mx<N and 0<=my<M:
                if MAP[mx][my]==1:
                    MAP[mx][my]=0
                    dq.append([mx,my])
cnt=0    
for i in range(N):
    for j in range(M):
        if MAP[i][j]==1:
            bfs(i,j)
            cnt+=1
            
print(cnt)
    
    