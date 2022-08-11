from collections import deque
import sys
input=sys.stdin.readline

dr=[(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]

N=int(input())
MAP=[[0 for _ in range(N)] for _ in range(N)]
a1,b1,a2,b2=map(int,input().split())

def bfs(x,y):
    dq=deque()
    dq.append([x,y])
    MAP[x][y]=1
    while dq:
        X,Y=dq.popleft()
        for a,b in dr:
            mx,my=X+a,Y+b
            if mx==a2 and my==b2:
                return MAP[X][Y]    
            if 0<=mx<N and 0<=my<N:
                if MAP[mx][my]==0:
                    MAP[mx][my]=MAP[X][Y]+1
                    dq.append([mx,my])
    return -1

print(bfs(a1,b1))