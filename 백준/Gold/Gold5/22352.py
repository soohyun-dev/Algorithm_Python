from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0), (0,1), (-1,0), (0,-1)]

N,M=map(int,input().split())
S=[list(map(int,input().split())) for _ in range(N)]
P=[list(map(int,input().split())) for _ in range(N)]

def bfs(s,p,x,y):
    dq=deque()
    dq.append([x,y])
    S[x][y]=p
    while dq:
        X,Y=dq.popleft()
        for a,b in dr:
            mx,my=X+a,Y+b
            if 0<=mx<N and 0<=my<M:
                if S[mx][my]==s :
                    S[mx][my]=p
                    dq.append([mx,my])
check=False   
for i in range(N):
    for j in range(M):
        if S[i][j]!=P[i][j]:
            bfs(S[i][j],P[i][j],i,j)
            check=True
            break
    if check==True:
        break
        
for i in range(N):
    for j in range(M):
        if S[i][j]!=P[i][j]:
            print('NO')
            exit(0)
            
print('YES')