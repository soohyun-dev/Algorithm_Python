from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque()

M,N=map(int,input().split())
maze=[]
for i in range(N):
    maze.append(list(map(int,input())))
def bfs():
    while dq:
        x,y=dq.popleft()
        if x==N-1 and y==M-1:
            break
        for i in range(4):
            mx=x+vertical[i]
            my=y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if maze[mx][my]==1:  # 벽을 부셔야 하는 경우 (가중치 1)
                    maze[mx][my]=maze[x][y]+1
                    dq.append([mx,my])
                elif maze[mx][my]==0: # 그냥 지나갈 수 있는 통로 (가중치 0)
                    maze[mx][my]=maze[x][y]
                    dq.appendleft([mx,my])  # 우선 탐색
                    
dq.append([0,0])  # 시작점 대입       
maze[0][0]=2  # 재탐색 방지
bfs()

print(maze[N-1][M-1]-2)