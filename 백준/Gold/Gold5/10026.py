from collections import deque

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]
dq=deque()
N=int(input())
RGB=[]
for _ in range(N):
    RGB.append(list(input()))
    
def bfs(word):
    global cnt
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            move_x=x+vertical[i]
            move_y=y+parallel[i]
            if 0<=move_x<N and 0<=move_y<N:
                if check==True:
                    if RGB[move_x][move_y]==word:
                        dq.append([move_x,move_y])
                        if word!='B':
                            RGB[move_x][move_y]='X'
                        elif word=='B':
                            RGB[move_x][move_y]='Y'
                else:
                    if RGB[move_x][move_y]==word:
                        dq.append([move_x,move_y])
                        if word=='X':
                            RGB[move_x][move_y]='O'
                        elif word=='Y':
                            RGB[move_x][move_y]='O'
    cnt+=1  
# 적록색약 아닌사람
cnt=1
check=True
for i in range(N):
    for j in range(N):
        if RGB[i][j]=='R':
            RGB[i][j]='X'
            dq.append([i,j])
            bfs('R')
        if RGB[i][j]=='G':
            RGB[i][j]='X'
            dq.append([i,j])
            bfs('G')
        if RGB[i][j]=='B':
            RGB[i][j]='Y'
            dq.append([i,j])
            bfs('B')
answer=[]
answer.append(cnt-1)
# 적록색약인 사람
cnt=1
check=False
for i in range(N):
    for j in range(N):
        if RGB[i][j]=='X':
            RGB[i][j]='O'
            dq.append([i,j])
            bfs('X')
        if RGB[i][j]=='Y':
            RGB[i][j]='O'
            dq.append([i,j])
            bfs('Y')
# B가 없는 경우 방지
if cnt==1:
    cnt=2
answer.append(cnt-1)
print(*answer)

