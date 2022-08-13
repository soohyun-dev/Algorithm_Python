from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0),(0,1),(-1,0),(0,-1)]

N,M,T=map(int,input().split())
MAP=[]
check=False
for i in range(N):
    L=list(map(int,input().split()))
    if check==False:
        for j in range(M):
            if L[j]==2:
                L[j]=-1
                check=True
    MAP.append(L)

def bfs():
    dq=deque()
    dq.append([0,0])
    MAP[0][0]=1
    S=0
    while dq:
        X,Y=dq.popleft()
        for a,b in dr:
            mx,my=X+a,Y+b
            if mx==N-1 and my==M-1:
                return [MAP[X][Y],S]
            if 0<=mx<N and 0<=my<M:
                if MAP[mx][my]==0:
                    MAP[mx][my]=MAP[X][Y]+1
                    dq.append([mx,my])
                elif MAP[mx][my]==-1:
                    S=MAP[X][Y]
                    MAP[mx][my]=MAP[X][Y]+1
                    S+=(N-1-mx)+(M-1-my)
                    dq.append([mx,my])
    return [0,S]

result=bfs()

if result[0]==0:
    tmp=result[1]
elif result[1]==0:
    tmp=result[0]
else:
    tmp=min(result)
    
if result==[0,0] or tmp>T:
    print('Fail')
else:
    print(tmp)