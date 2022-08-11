from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0),(0,1),(-1,0),(0,-1)]

N,M=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(N)]
S=[[[0,0] for _ in range(M)] for _ in range(N)]
D=[[0 for _ in range(M)] for _ in range(N)]

def bfs(x,y,C):
    dq=deque()
    dq.append([x,y])
    visited=[[0 for _ in range(M)] for _ in range(N)]
    visited[x][y]=1
    cnt=0
    store=[[x,y]]
    while dq:
        X,Y=dq.popleft()
        for a,b in dr:
            mx,my=X+a,Y+b
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==0:
                    if visited[mx][my]==0:
                        dq.append([mx,my])
                        store.append([mx,my])
                        visited[mx][my]=1
                        cnt+=1
    for a,b in store:
        S[a][b][0]=cnt+1
        S[a][b][1]=C

c=1
for i in range(N):
    for j in range(M):
        if MAP[i][j]==0:
            bfs(i,j,c)
            c+=1

for i in range(N):
    for j in range(M):
        if S[i][j][0]==0:
            tmp=[]
            for a,b in dr:
                mi,mj=i+a,j+b
                if 0<=mi<N and 0<=mj<M:
                    if S[mi][mj][1] not in tmp:
                        D[i][j]+=S[mi][mj][0]
                        tmp.append(S[mi][mj][1])
            D[i][j]+=1
        print(D[i][j]%10,end='')
    print()

for i in range(N):
    print(S[i])