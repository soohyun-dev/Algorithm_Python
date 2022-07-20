from collections import deque
import copy

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque()

N=int(input())
place=[]
MAX=0
for i in range(N):
    place.append(list(map(int,input().split())))
    # 가장 높은 높이 저장
    if MAX<max(place[i]):
        MAX=max(place[i])
    
    
def bfs(num):
    global cnt
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            move_x=x+vertical[i]
            move_y=y+parallel[i]
            if 0<=move_x<N and 0<=move_y<N:
                if check[move_x][move_y]>num:
                    dq.append([move_x,move_y])
                    check[move_x][move_y]=0
    cnt+=1

# result 초기값을 0으로 잡으면 틀림, 테스트 케이스에는 최소 한구역 이상의 안전구역이 있음.
result=[1]
for i in range(1,MAX):
    cnt=0
    # 원래의 표 보존을 위해 deepcopy 사용
    check=copy.deepcopy(place)
    for j in range(N):
        for k in range(N):
            if check[j][k]>i:
                dq.append([j,k])
                bfs(i)
    result.append(cnt)
    
print(max(result))