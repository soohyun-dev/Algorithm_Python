from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

R,C=map(int,input().split())
MAP=[list(input().rstrip()) for _ in range(R)]

def bfs(x):
    boo=False
    if x==dq1:
        while dq1:
            X,Y=dq1.popleft()
            for i in range(4):
                mx,my=X+vertical[i],Y+parallel[i]
                if 0<=mx<R and 0<=my<C:
                    if MAP[mx][my]=='.' or MAP[mx][my]=='S':
                        boo=True
                        MAP[mx][my]='*'
    elif x==dq2:
        while dq2:
            X,Y=dq2.popleft()
            for i in range(4):
                mx,my=X+vertical[i],Y+parallel[i]
                if 0<=mx<R and 0<=my<C:
                    if MAP[mx][my]=='.':
                        MAP[mx][my]='S'
                        boo=True
                    if MAP[mx][my]=='D':
                        return True
    if boo==False:
        return 'KAKTUS'
    
    return None
    
dq1=deque()  # 물
dq2=deque()  # 고슴도치

visited=[[False for _ in range(R)] for _ in range(C)]
cnt=0
while True:
    for i in range(R):
        for j in range(C):
            if MAP[i][j]=='*':
                dq1.append([i,j])
            if MAP[i][j]=='S':
                dq2.append([i,j])
    bfs(dq1)
    result=bfs(dq2)
    cnt+=1
    if result==True:
        print(cnt)
        break
    if result=='KAKTUS':
        print('KAKTUS')
        exit(0)
    