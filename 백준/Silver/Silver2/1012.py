from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque() 
def check(i,j):
    dq.append([i,j])
    while dq:
        i,j=dq.popleft()
        for k in range(4):
            move_x=i+vertical[k]
            move_y=j+parallel[k]
            if 0<=move_x<N and 0<=move_y<M:
                if place[move_x][move_y]==1:
                    dq.append([move_x,move_y])
                    place[move_x][move_y]=0
                

for _ in range(int(input())):
    M,N,K=map(int,input().split())
    place=[[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        place[y][x]=1
    cnt=0
    for i in range(N):
        for j in range(M):
            if place[i][j]==1:
                place[i][j]=0
                check(i,j)
                cnt+=1
    print(cnt)
    
    

       
    
    
    
    
    