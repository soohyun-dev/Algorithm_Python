from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque()
result=[]  # 영역의 크기 저장할 공간

N,M,K=map(int,input().split())
paper=[[0 for _ in range(M)]for _ in range(N)]
for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(y1,y2):  # 입력받은 직사각형들 표에 덮어씌우기
        for k in range(x1,x2):
            paper[j][k]=1

def bfs():
    cnt=1
    while dq:
        y,x=dq.popleft()  # y,x 위치 조심!
        for i in range(4):
            my=y+vertical[i]  # 위아래
            mx=x+parallel[i]  # 좌우
            if 0<=my<N and 0<=mx<M:
                if paper[my][mx]==0:
                    dq.append([my,mx])
                    paper[my][mx]=2
                    cnt+=1 
    result.append(cnt)  # 한 영역의 크기 저장
    
for i in range(N):
    for j in range(M):
        if paper[i][j]==0:
            dq.append([i,j])
            paper[i][j]=2
            bfs()
result.sort()  # 정렬
print(len(result))  # 영역이 저장된 수만큼이 영역의 개수
print(*result)