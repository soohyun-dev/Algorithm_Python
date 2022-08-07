from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,L,R=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]

def bfs(x,y):
    SUM=0
    store=[]
    dq=deque()
    visited[x][y]=True
    dq.append([x,y])
    store.append([x,y])
    SUM+=MAP[x][y]
    while dq:
        X,Y=dq.popleft()
        for i in range(4):
            mx,my=X+vertical[i],Y+parallel[i]
            if 0<=mx<N and 0<=my<N:
                if visited[mx][my]==False:
                    tmp=abs(MAP[X][Y]-MAP[mx][my])
                    if tmp>=L and tmp<=R:
                        SUM+=MAP[mx][my]
                        dq.append([mx,my])
                        store.append([mx,my])
                        visited[mx][my]=True
    if len(store)!=1:
        a=SUM//len(store)
        for i in range(len(store)):
            MAP[store[i][0]][store[i][1]]=a
        return True
    else:
        return False
    
cnt=0
while True:
    visited=[[False for _ in range(N)] for _ in range(N)]
    result=[]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==False:
                result.append(bfs(i,j))
    if True not in result:
        break
    cnt+=1

print(cnt)
        