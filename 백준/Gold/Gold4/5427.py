from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0),(0,1),(-1,0),(0,-1)]

for _ in range(int(input())):
    w,h=map(int,input().split())
    MAP=[list(input().rstrip()) for _ in range(h)]
    dq=deque()
    def bfs(x,y):
        dq1=deque()
        dq.appendleft([x,y])
        dq1.append([x,y])
        MAP[x][y]=1
        while dq:
            X,Y=dq.popleft()
            if len(dq1)==0:
                return "IMPOSSIBLE"
            if type(MAP[X][Y])==int:
                if X==0 or X==h-1 or Y==0 or Y==w-1:
                    return MAP[X][Y]
            for a,b in dr:
                mx,my=X+a,Y+b
                if 0<=mx<h and 0<=my<w:          
                    if MAP[X][Y]=='*':
                        if MAP[mx][my]!='#' and MAP[mx][my]!='*':
                            MAP[mx][my]='*'
                            dq.append([mx,my])
                    elif type(MAP[X][Y])==int:
                        if MAP[mx][my]=='.':
                            dq1.popleft()
                            MAP[mx][my]=1
                            dq.append([mx,my])
                            dq1.append((mx,my)) 
        return 'IMPOSSIBLE'
        
    for i in range(h):
        for j in range(w):
            if MAP[i][j]=='*':
                dq.append([i,j])
            elif MAP[i][j]=='@':
                x,y=i,j
                
    print(bfs(x,y))
