from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0), (0,1), (-1,0), (0,-1)]

N,M=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(N)]

def bfs(x,y):
    dq=deque()
    dq.append([x,y])
    while dq:
        X,Y=dq.popleft()
        if X==N-1:
            print('YES')
            exit(0)
        for a,b in dr:
            mx,my=X+a,Y+b
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==0:
                    MAP[mx][my]=1
                    dq.append([mx,my])

for i in range(M):
    if MAP[0][i]==0:
        bfs(0,i)

print('NO')