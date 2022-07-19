from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
upDown=[0,1,-1]
box=[]
dq=deque()
M,N,H=map(int,input().split())
cnt=0
def bfs():
    global cnt
    while dq:
        z,x,y=dq.popleft()
        for i in range(3):
            if i==0:
                for j in range(4):
                    move_x=x+vertical[j]
                    move_y=y+parallel[j]
                    if 0<=move_x<N and 0<=move_y<M:
                        if box[z][move_x][move_y]==0:
                            box[z][move_x][move_y]=box[z][x][y]+1
                            dq.append([z,move_x,move_y])
            else:
                for k in range(1,3):
                    move_z=z+upDown[k]
                    if 0<=move_z<H:
                        if box[move_z][x][y]==0:
                            box[move_z][x][y]=box[z][x][y]+1
                            dq.append([move_z,x,y])
for _ in range(H):
    tmp=[]
    for _ in range(N):
        tmp.append(list(map(int,input().split())))
    box.append(tmp)

for i in range(H):    
    for j in range(N):
        for k in range(M):
            if box[i][j][k]==1:
                dq.append([i,j,k])
bfs()
check=False
MAX=0

for i in range(H):
    for j in range(N):
        for k in box[i][j]:
            if k==0:
                print(-1)
                exit(0)
            if k==2:
                check=True
            if k>MAX:
                MAX=k
if check==False:
    print(0)
else:
    print(MAX-1)
    

            
        