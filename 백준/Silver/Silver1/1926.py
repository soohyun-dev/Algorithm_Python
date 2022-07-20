from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque()

N,M=map(int,input().split())
paper=[]
for _ in range(N):
    paper.append(list(map(int,input().split())))
result=[0]  # 그림이 하나도 없는 경우를 방지, 초기값 0 대입

def bfs():
    cnt=1
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            move_x=x+vertical[i]
            move_y=y+parallel[i]
            if 0<=move_x<N and 0<=move_y<M:
                if paper[move_x][move_y]==1:
                    dq.append([move_x,move_y])
                    paper[move_x][move_y]=2
                    cnt+=1
    result.append(cnt)

for i in range(N):
    for j in range(M):
        if paper[i][j]==1:
            dq.append([i,j])
            
            bfs()

print(len(result)-1)
print(max(result))
            