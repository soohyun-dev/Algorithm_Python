from collections import deque
import copy

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M=map(int,input().split())
place=[]
cnt=0
for i in range(N):
    place.append(list(map(int,input())))
    cnt+=place[i].count(1)
place[0][0]=-1
visitied=[[False for _ in range(M)] for _ in range(N)]
    
boo=False
result=[]
MAX=0
def bfs():
    global Skill, boo, MAX
    MAP=copy.deepcopy(place)
    dq=deque()
    dq.append([0,0])
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            move_x=x+vertical[i]
            move_y=y+parallel[i]
            if 0<=move_x<N and 0<=move_y<M:
                if move_x==N-1 and move_y==M-1:
                    MAP[move_x][move_y]=MAP[x][y]+1
                    if MAX<MAP[move_x][move_y]+2:
                        MAX=MAP[move_x][move_y]+2
                    boo=True
                    break
                if Skill==True:
                    if MAP[move_x][move_y]==0:
                        MAP[move_x][move_y]=MAP[x][y]+1
                        dq.append([move_x,move_y])
                    elif MAP[move_x][move_y]==1:
                        if visitied[move_x][move_y]==False:
                            Skill=False
                            visitied[move_x][move_y]=True 
                            MAP[move_x][move_y]=MAP[x][y]+1
                            dq.append([move_x,move_y])
                else:
                    if MAP[move_x][move_y]==0 :
                        MAP[move_x][move_y]=MAP[x][y]+1
                        dq.append([move_x,move_y])
        if boo==True:
            break

for i in range(cnt):
    Skill=True
    bfs() 
        
if MAX==0:
    print(-1)
else:
    print(MAX)