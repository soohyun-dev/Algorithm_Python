from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0),(0,1),(-1,0),(0,-1)]

N,M=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(N)]
S=[[0 for _ in range(M)] for _ in range(N)]

def bfs(x,y,C):
    dq=deque()
    dq.append([x,y])
    visited[x][y]=1
    cnt=1
    S[x][y]=C
    while dq:
        X,Y=dq.popleft()
        for a,b in dr:
            mx,my=X+a,Y+b
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==0:
                    if visited[mx][my]==0:
                        MAP[mx][my]=1
                        dq.append([mx,my])
                        visited[mx][my]=1
                        cnt+=1
                        S[mx][my]=C
    return cnt
c=1
MAX=0
dict={}
visited=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if MAP[i][j]==0:
            result=bfs(i,j,c)
            dict[c]=result
            c+=1

for i in range(N):
    for j in range(M):
        D=0
        tmp=set()
        if S[i][j]==0:
            for a,b in dr:
                mi,mj=i+a,j+b
                if 0<=mi<N and 0<=mj<M:
                    if S[mi][mj]!=0:
                        tmp.add(S[mi][mj])
            for m in tmp:
                D+=dict[m]
            D+=1
        print(D%10,end='')
    print()