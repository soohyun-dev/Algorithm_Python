from collections import deque
import copy

dq=deque()
N,M=map(int,input().split())
place=[]
parallel=[0,0,1,-1]
vertical=[1,-1,0,0]

for i in range(N):
    place.append(list(map(int,input().split())))
    
def wall(cnt):  # 벽 세우기
    # 벽이 다 세워졌을 때
    if cnt==3:
        diffuse()
        return
    
    for i in range(N):
        for j in range(M):
            if place[i][j]!=1 and place[i][j]!=2 and cnt!=3:
                place[i][j]=1
                wall(cnt+1)
                place[i][j]=0    
                
def safe(check):  # 안전구역 체크
    global result
    tmp=0
    for i in check:
        tmp+=i.count(0)
    if tmp > result:
        result=tmp

def diffuse():  # 바이러스 퍼트리기
    check=copy.deepcopy(place)
    # 바이러스 위치 파악
    for i in range(N):
        for j in range(M):
            if check[i][j]==2:
                dq.append([i,j])
    # 바이러스 퍼트리기 시작
    while dq: 
        i,j=dq.popleft()           
        for k in range(4):
            move_x=i+vertical[k]
            move_y=j+parallel[k]
            if 0 <= move_x <N and 0 <= move_y < M:
                if check[move_x][move_y]==0:
                    check[move_x][move_y]=2
                    dq.append([move_x,move_y])
    # 안전구역 체크
    safe(check)
                
result=0     
wall(0)
print(result)             



