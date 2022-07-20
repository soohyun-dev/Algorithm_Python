from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque()
result=[]

N,M,K=map(int,input().split())
paper=[[0 for _ in range(M)]for _ in range(N)]
for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            paper[j][k]=1

def bfs():
    cnt=1
    while dq:
        y,x=dq.popleft()
        for i in range(4):
            mx=x+parallel[i]
            my=y+vertical[i]
            if 0<=my<N and 0<=mx<M:
                if paper[my][mx]==0:
                    dq.append([my,mx])
                    paper[my][mx]=2
                    cnt+=1
    result.append(cnt)
    
    
for i in range(N):
    for j in range(M):
        if paper[i][j]==0:
            dq.append([i,j])
            paper[i][j]=2
            bfs()
result.sort()
print(len(result))
print(*result)