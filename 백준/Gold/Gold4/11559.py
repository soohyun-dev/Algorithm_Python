from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0),(0,1),(-1,0),(0,-1)]

MAP=[list(input().rstrip()) for _ in range(12)]

def bfs(T,x,y):
    dq=deque()
    dq.append([x,y])
    store=[(x,y)]
    visited=[[0 for _ in range(12)] for _ in range(12)]
    visited[x][y]=1
    cnt=1
    while dq:
        X,Y=dq.popleft()
        for a,b in dr:
            mx,my=X+a,Y+b
            if 0<=mx<12 and 0<=my<6:
                if MAP[mx][my]==T and not visited[mx][my]:
                    store.append((mx,my))
                    cnt+=1
                    dq.append([mx,my])
                    visited[mx][my]=1
    if cnt>=4:
        for n,m in store:
            MAP[n][m]='.'
        return True
    return False

C=0
while True:
    L=[]
    check=False
    for i in range(11,-1,-1):
        for j in range(6):
            if MAP[i][j]!='.':
                result=bfs(MAP[i][j],i,j)
                if result==True:
                    check=True
    for i in range(6):
        tmp=0
        CK=False
        j=11
        while True:
            if MAP[j][i]=='.':
                tmp+=1
                CK=True
                j-=1
            else:
                if CK==True:
                    MAP[j][i],MAP[j+tmp][i]=MAP[j+tmp][i],MAP[j][i]
                    j=j+tmp
                    tmp=0
                    CK=False
                else:
                    j-=1
            if j==-1:
                break
    if check==False:
        print(C)
        break
    C+=1