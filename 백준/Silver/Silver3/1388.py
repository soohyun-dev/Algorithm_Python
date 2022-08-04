from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
MAP=[list(input()) for _ in range(N)]

def bfs(x,y,a):
    dq=deque()
    dq.append([x,y])
    while dq:
        X,Y=dq.popleft()
        MAP[X][Y]=0
        if a=='-':
            if 0<=X<N and 0<=Y+1<M:
                if MAP[X][Y+1]=='-':
                    MAP[X][Y+1]=0
                    dq.append([X,Y+1])
        elif a=='|':
            if 0<=X+1<N and 0<=Y<M:
                if MAP[X+1][Y]=='|':
                    MAP[X+1][Y]=0
                    dq.append([X+1,Y])

cnt=0
for i in range(N):
    for j in range(M):
        if MAP[i][j]=='-' or MAP[i][j]=='|':
            result=bfs(i,j,MAP[i][j])
            cnt+=1
            
print(cnt)