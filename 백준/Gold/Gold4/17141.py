from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
from itertools import combinations

vertical=[1,-1,0,0]
parallel=[0,0,1,-1]

N,M=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]
dq=deque()

def bfs(LIST,MAP):
    cnt=0
    virusMAP=deepcopy(MAP)
    for i in range(len(LIST)):
        dq.append(LIST[i])
        virusMAP[LIST[i][0]][LIST[i][1]]=1
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            X,Y=x+vertical[i], y+parallel[i]
            if 0<=X<N and 0<=Y<N:
                if virusMAP[X][Y]==0:
                    dq.append([X,Y])
                    virusMAP[X][Y]=virusMAP[x][y]+1          
                    if cnt<virusMAP[X][Y]:
                        cnt=virusMAP[X][Y]

    for i in range(N):
        for j in range(N):
            if virusMAP[i][j]==0:
                cnt=-1
    return cnt   

virus=[]
for i in range(N):
    for j in range(N):
        if MAP[i][j]==2:
            virus.append([i,j]) 
            MAP[i][j]=0

result=[]
LIST=list(combinations(virus,M))
for i in range(len(LIST)):
    result.append(bfs(LIST[i], MAP))
if len(result)==1 and result==[0]:
    print(0)
else:
    remove_set={-1}
    if -1 in result:
        result=[i for i in result if i not in remove_set]
        if len(result)==0:
            print(-1)
            exit(0)

    print(min(result)-1)
