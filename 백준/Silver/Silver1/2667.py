from collections import deque

N=int(input())
place=[]
for i in range(N):
    place.append(list(map(int,input())))

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque()

def numChange(i,j,cnt):
    dq.append([i,j])
    while dq:
        i,j=dq.popleft()
        for k in range(4):
            move_x=i+vertical[k]
            move_y=j+parallel[k]
            if 0<=move_x<N and 0<=move_y<N:
                if place[move_x][move_y]==1:
                    place[move_x][move_y]=cnt
                    dq.append([move_x,move_y])

cnt=2
for i in range(N):
    for j in range(N):
        if place[i][j]==1:
            place[i][j]=cnt
            numChange(i,j,cnt)
            cnt+=1

complex=cnt-2
print(complex)
num=2
answer=[]
for i in range(complex):
    result=0
    for j in range(N):
        result+=place[j].count(num)
    answer.append(result)
    num+=1

answer.sort()
for i in range(complex):
    print(answer[i])
    
    
    