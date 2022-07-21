from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque()

M,N=map(int,input().split())
maze=[]
for i in range(N):
    maze.append(list(map(int,input())))
def bfs():
    global cnt
    while dq:
        x,y=dq.popleft()
        if x==N-1 and y==M-1:
            break
        for i in range(4):
            mx=x+vertical[i]
            my=y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if maze[mx][my]==1:
                    maze[mx][my]=maze[x][y]+1
                    dq.append([mx,my])
                elif maze[mx][my]==0:
                    maze[mx][my]=maze[x][y]
                    dq.appendleft([mx,my])
dq.append([0,0])       
maze[0][0]=2
cnt=0
bfs()

print(maze[N-1][M-1]-2)