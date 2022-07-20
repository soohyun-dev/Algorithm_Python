from ipaddress import collapse_addresses

from collections import deque

vertical=[1,2,2,1,-1,-2,-2,-1]
parallel=[-2,-1,1,2,2,1,-1,-2]
for _ in range(int(input())):
    dq=deque()
    N=int(input())
    chess=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(2):
        a,b=map(int,input().split())
        if i==0:
            dq.append([a,b])
        else:
            chess[a][b]=-1
    if dq[0]==[a,b]:
        print(0)
    else:
        check=False
        while dq:
            x,y=dq.popleft()
            for i in range(8):
                move_x=x+vertical[i]
                move_y=y+parallel[i]
                if 0<=move_x<N and 0<=move_y<N:
                    if chess[move_x][move_y]==0:
                        dq.append([move_x, move_y])
                        chess[move_x][move_y]=chess[x][y]+1
                    if chess[move_x][move_y]==-1:
                        print(chess[x][y]+1)
                        check=True
                        break
            if check==True:
                break