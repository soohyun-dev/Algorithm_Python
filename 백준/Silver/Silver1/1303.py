from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

M,N=map(int,input().split())
MAP=[list(input()) for _ in range(N)]

def bfs(x,y,a):
    dq=deque()
    dq.append([x,y])
    MAP[x][y]=0
    cnt=1
    while dq:
        X,Y=dq.popleft()
        for i in range(4):
            mx,my=X+vertical[i],Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==a:
                    MAP[mx][my]=0
                    cnt+=1
                    dq.append([mx,my])
    return cnt**2

answer=[0,0]
for i in range(N):
    for j in range(M):
        if MAP[i][j]=='W':
            answer[0]+=bfs(i,j,'W')
        elif MAP[i][j]=='B':
            answer[1]+=bfs(i,j,'B')

print(*answer)