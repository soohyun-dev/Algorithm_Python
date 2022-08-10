from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0),(0,1),(-1,0),(0,-1)]

N,M,K=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(N)]
visited=[[K+1 for _ in range(M)] for _ in range(N)]

dq=deque()
dq.append([0,0,0,0])
visited[0][0]=0
while dq:
    for i in range(N):
        print(visited[i])
    print()
    X,Y,Z,C=dq.popleft()   
    if X==N-1 and Y==M-1:
        print(C+1)
        exit(0)
    for a,b in dr:
        mx,my=X+a,Y+b
        if 0<=mx<N and 0<=my<M:
            if visited[mx][my]>Z:
                if MAP[mx][my]==0:
                    visited[mx][my]=Z
                    dq.append([mx,my,Z,C+1])
                else:
                    if C%2==0:  # 낮 
                        if Z<K: 
                            visited[mx][my]=Z
                            dq.append([mx,my,Z+1,C+1])
                    else:  # 밤
                         dq.append([X,Y,Z,C+1])
print(-1)