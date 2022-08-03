from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N=int(input())
MAP=[list(map(int,input().rstrip())) for _ in range(N)]

def bfs(x,y):
    dq=deque()
    dq.append([x,y])
    visited=[[[0,0] for _ in range(N)] for _ in range(N)]
    visited[0][0][0]=1
    while dq:
        X,Y=dq.popleft()
        for i in range(4):
            mx,my=X+vertical[i],Y+parallel[i]
            if 0<=mx<N and 0<=my<N:
                if visited[mx][my][0]==0:
                    if MAP[mx][my]==0:
                        dq.append([mx,my])
                        visited[mx][my][0]=1
                        visited[mx][my][1]=visited[X][Y][1]+1
                    elif MAP[mx][my]==1:
                        dq.append([mx,my])
                        visited[mx][my][0]=1
                        visited[mx][my][1]=visited[X][Y][1]
                else:
                    if MAP[mx][my]==0 and visited[mx][my][1]>visited[X][Y][1]:
                        dq.append([mx,my])
                        visited[mx][my][1]=visited[X][Y][1]+1
                    elif MAP[mx][my]==1 and visited[mx][my][1]>visited[X][Y][1]:
                        dq.append([mx,my])
                        visited[mx][my][1]=visited[X][Y][1]
                    
    for i in range(N):
        print(visited[i])
    return visited[N-1][N-1][1]

print(bfs(0,0))

