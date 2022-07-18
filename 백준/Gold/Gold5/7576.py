from collections import deque

vertical=[0,1,-1,0]
parallel=[1,0,0,-1]
dq=deque()

M,N=map(int,input().split())
place=[]
for _ in range(N):
    place.append(list(map(int,input().split())))
    
def check():
    while dq:
        i,j = dq.popleft()
        for k in range(4):
            move_x=i+vertical[k]
            move_y=j+parallel[k]
            if 0<=move_x<N and 0<=move_y<M:
                if place[move_x][move_y]==0:
                    dq.append([move_x,move_y])
                    place[move_x][move_y]=place[i][j]+1

for i in range(N):
    for j in range(M):
        if place[i][j]==1:
            dq.append([i,j])

check()

answer=0
boo=True
for i in range(N):
    for j in place[i]:
        if j>answer:
            answer=j
        if j==0:
            print(-1)
            exit(0)

print(answer-1)

