from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0), (0,1), (-1,0), (0,-1)]

N,K=map(int,input().split())
MAP=[]
tmp=[]
visited=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    L=list(map(int,input().split()))
    for j in range(N):
        if L[j]!=0:
            tmp.append([L[j],i,j])
    MAP.append(L)
tmp.sort(key=lambda x:x[0])
dq=deque()
for k in range(len(tmp)):
    dq.append([tmp[k][0],tmp[k][1],tmp[k][2]])
    visited[tmp[k][1]][tmp[k][2]]=1
    
S,A,B=map(int,input().split())
while dq:
    Z,X,Y=dq.popleft()
    for a,b in dr:
        mx,my=X+a,Y+b
        if 0<=mx<N and 0<=my<N:
            if MAP[mx][my]==0:
                MAP[mx][my]=Z
                visited[mx][my]=visited[X][Y]+1
                dq.append([Z,mx,my])
                
for i in range(N):
    print(visited[i])
print()
for i in range(N):
    print(MAP[i])

if visited[A-1][B-1]>S+1:
    print(0)
else:
    print(MAP[A-1][B-1])