from collections import deque

vertical=[1,-1,0,0,-1,-1,1,1]
parallel=[0,0,1,-1,-1,1,-1,1]
dq=deque()

def bfs():
    global cnt
    while dq:
        x,y=dq.popleft()
        for i in range(8):
            move_x=x+vertical[i]
            move_y=y+parallel[i]
            if 0<=move_x<h and 0<=move_y<w and place[move_x][move_y]==1:
                place[move_x][move_y]=cnt
                dq.append([move_x,move_y])
    cnt+=1

while True:
    cnt=2
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    place=[]
    if w==1:
        place.append(list(map(int,input())))
    else:
        for _ in range(h):
            place.append(list(map(int,input().split())))
        
    for i in range(h):
        for j in range(w):
            if place[i][j]==1:
                dq.append([i,j])
                place[i][j]=cnt
                bfs()
                
    if cnt==2:
        print(0)
    else:
        print(cnt-2)
    
    