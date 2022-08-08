from collections import deque
import sys
input=sys.stdin.readline

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
upDown=[1,-1]

while True:
    L,R,C=map(int,input().rstrip().split())
    if L==0 and R==0 and C==0:
        break
    MAP=[[list(input()) for _ in range(R+1)] for _ in range(L)]
    
    def bfs(z,x,y):
        dq=deque()
        dq.append([z,x,y])
        MAP[z][x][y]=0
        while dq:
            Z,X,Y=dq.popleft()
            for i in range(4):
                mx,my=X+vertical[i],Y+parallel[i]
                if 0<=Z<L and 0<=mx<R and 0<=my<C:
                    if MAP[Z][mx][my]=='.':
                        MAP[Z][mx][my]=MAP[Z][X][Y]+1
                        dq.append([Z,mx,my])
                    if MAP[Z][mx][my]=='E':
                        return MAP[Z][X][Y]+1
            for j in range(2):
                mz=Z+upDown[j]
                if 0<=mz<L and 0<=X<R and 0<=Y<C:
                    if MAP[mz][X][Y]=='.':
                        MAP[mz][X][Y]=MAP[Z][X][Y]+1
                        dq.append([mz,X,Y])       
                    if MAP[mz][X][Y]=='E':
                        return MAP[Z][X][Y]+1       
        return False
                             
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if MAP[i][j][k]=='S':
                    result=bfs(i,j,k)
                    if result==False:
                        print('Trapped!')
                    else:
                        print('Escaped in %d minute(s).' %(result))