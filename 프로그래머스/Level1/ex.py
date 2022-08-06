from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
upDown=[1,2,2,1,-1,-2,-2,-1]
leftRight=[-2,-1,1,2,2,1,-1,-2]

K=int(input())
M,N=map(int,input().split())
MAP=[list(map(int,input().rstrip().split())) for _ in range(N)]
visited=[[[0]*(K+1) for _ in range(M)] for _ in range(N)]

dq=deque()
def bfs():
    dq.append([0,0,0])
    visited[0][0][0]=1
    while dq:
        X,Y,Z=dq.popleft()
        if X==N-1 and Y==M-1:
            print(visited[X][Y][Z])
            exit(0)
        if Z<K:
            for j in range(8):
                mx,my=X+upDown[j],Y+leftRight[j]
                if 0<=mx<N and 0<=my<M:
                    if MAP[mx][my]==0 and visited[mx][my][Z+1]==0:
                        visited[mx][my][Z+1]=visited[mx][my][Z]+1
                        dq.append([mx,my,Z+1])
        for i in range(4):
            mx,my=X+vertical[i],Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==0:
                    if visited[mx][my][Z]==0:
                        dq.append([mx,my,Z])
                        visited[mx][my][Z]=visited[X][Y][Z]+1
    print(-1)
    
bfs()