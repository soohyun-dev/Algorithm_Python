from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M=map(int,input().split())
MAP=[list(input()) for _ in range(N)]

def bfs(x,y):
    dq=deque()
    dq.append([x,y])
    wolf=0
    sheep=0
    if MAP[x][y]=='v':
        wolf+=1
    elif MAP[x][y]=='k':
        sheep+=1
    MAP[x][y]=0
    while dq:
        X,Y=dq.popleft()
        for i in range(4):
            mx,my=X+vertical[i],Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]=='.' or MAP[mx][my]=='v' or MAP[mx][my]=='k':
                    if MAP[mx][my]=='v':
                        wolf+=1
                    elif MAP[mx][my]=='k':
                        sheep+=1
                    dq.append([mx,my])
                    MAP[mx][my]=0
    if wolf < sheep:
        return ['sheep', sheep]
    else:
        return ['wolf', wolf]
                
answer=[0,0]
for i in range(N):
    for j in range(M):
        if MAP[i][j]=='.' or MAP[i][j]=='v' or MAP[i][j]=='k':
            result=bfs(i,j) 
            if result[0]=='sheep':
                answer[0]+=result[1]
            elif result[0]=='wolf':
                answer[1]+=result[1]

print(*answer)