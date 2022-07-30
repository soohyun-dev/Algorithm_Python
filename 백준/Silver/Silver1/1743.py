from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M,K=map(int,input().rstrip().split())
MAP=[['.' for _ in range(M)] for _ in range(N)]
for i in range(K):
    a,b=map(int,input().split())
    MAP[a-1][b-1]='#'
    
def bfs(x,y):
    dq=deque()
    dq.append([x,y])
    cnt=1
    while dq:
        X,Y = dq.popleft()
        for i in range(4):
            mx,my=X+vertical[i], Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]=='#':
                    MAP[mx][my]='.'
                    dq.append([mx,my])
                    cnt+=1
    return cnt

MAX=0
for i in range(N):
    for j in range(M):
        if MAP[i][j]=='#':
            MAP[i][j]='.'
            result=bfs(i,j)
            if MAX<result:
                MAX=result

print(MAX)