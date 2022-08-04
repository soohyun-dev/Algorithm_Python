from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M=map(int,input().split())
MAP=[]
first=0
for i in range(N):
    MAP.append(list(map(int,input().split())))
    first+=MAP[i].count(1)  # 초기 치즈 갯수 세두기
    
def bfs(x,y):
    dq=deque()
    dq.append([x,y])
    visited=[[False]*M for _ in range(N)]
    while dq:
        X,Y=dq.popleft()
        for i in range(4):
            mx=X+vertical[i]
            my=Y+parallel[i]
            if 0<=mx<N and 0<=my<M:
                if visited[mx][my]==False:
                    if MAP[mx][my]==1 and MAP[X][Y]==0:
                            visited[mx][my]=True
                            MAP[mx][my]=0
                    elif MAP[mx][my]==0:
                        dq.append([mx,my])
                        visited[mx][my]=True
                        MAP[mx]
    cnt=0
    for i in range(N):  # 녹고 남은 치즈 세기
        cnt+=MAP[i].count(1)
    return cnt
    
answer=[]  # 줄어드는 치즈값 저장
while True:
    result=bfs(0,0)
    if result==0:  # 치즈가 다 녹았을 시
        if len(answer)>0:
            print(len(answer)+1)
            print(answer[-1])  # 이전 치즈 갯수 출력
            break
        else:  # 치즈가 한 번에 다 녹아버린 경우
            print(1)
            print(first)  # 맨 처음 치즈 갯수를 출력해주자.
            break
    else:
        answer.append(result)

