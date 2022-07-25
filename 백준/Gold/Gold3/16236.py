from collections import deque
import sys

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
N=int(input())
ocean=[]  # 리스트 저장
fish=0  # 물고기 수
x,y=0,0  # 아기 상어 위치
babyShark=2  # 아기 상어 크기
time=0  # 걸린 시간
eatCnt=0  # 먹은 물고기 수

for i in range(N):
    ocean.append(list(map(int,input().split())))
    for j in range(N):
        if ocean[i][j]!=0 and ocean[i][j]!=9:  # 물고기 수 카운트
            fish+=1
        elif ocean[i][j]==9:  # 처음 아기 상어 위치 저장
            x=i
            y=j
            ocean[i][j]=0  # 현재자리 빈곳으로 초기화

def bfs(x,y):
    dq=deque()
    dq.append([x,y,0]) 
    visited=[[False]*N for _ in range(N)]
    visited[x][y]=True
    MIN=sys.maxsize
    fishInfo=[]  #
    while dq:
        X,Y,dist=dq.popleft()
        for i in range(4):
            mx=X+vertical[i]
            my=Y+parallel[i]
            if 0<=mx<N and 0<=my<N and visited[mx][my]==False:  # 갈 수 있는 자리인지 확인
                if ocean[mx][my]<=babyShark:  #  아기상어 크기 이하인 물고기가 존재하는가?
                    visited[mx][my]=True
                    if 0<ocean[mx][my]<babyShark:  # 먹을 수 있는 물고기 인가?
                        MIN=dist
                        fishInfo.append((mx,my,dist+1))
                    if dist+1<=MIN:
                        dq.append([mx,my,dist+1])
    if fishInfo:
        fishInfo.sort(key=lambda x:(x[2],x[0],x[1]))  # 1. 거리순, 2. 행 순 3. 열 순
        return fishInfo[0]  # 첫번째 값만 리턴
    else:
        return False  # 물고기가 없을 시
    
while fish:
    result=bfs(x,y)
    print(result)
    if not result:
        break
    x,y=result[0],result[1]
    ocean[x][y]=0  # 잡아먹혔다 표시
    time+=result[2]  # 거리만큼 시간 증가
    fish-=1  # 물고기 수 감소
    eatCnt+=1  # 먹은 숫자 증가
    if babyShark==eatCnt:  # 아기상어 몸집과 먹은 수가 동일할 시 몸집+1
        babyShark+=1
        eatCnt=0
print(time)