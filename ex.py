from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M,K=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(N)]
visited=[[[0]*(K+1) for _ in range(M)] for _ in range(N)]

def bfs():
    time=-1
    cnt=1
    dq=deque()
    dq.append([0,0,0,time,cnt])
    while dq:
        X,Y,Z,T,C=dq.popleft()
        visited[X][Y][Z]=1
        T=T*(-1)
        for i in range(4):
            mx,my=X+vertical[i],Y+parallel[i]
            if mx==N-1 and my==M-1:
                print(C+1)
                exit(0)
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==0 and visited[mx][my][Z]==0:
                    dq.append([mx,my,Z,T,C+1])
                    visited[mx][my][Z]=visited[X][Y][Z]+1
                elif MAP[mx][my]==1:
                    if Z<K and T==1:
                        dq.append([mx,my,Z+1,T,C+1])
                        visited[mx][my][Z+1]=visited[X][Y][Z]+1
                    if Z<K and T==-1:
                        dq.append([X,Y,Z,T,C+1])
                        visited[X][Y][Z]+=1
    print(-1)
bfs()