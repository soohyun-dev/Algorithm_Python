from cmath import inf
from collections import deque
import sys
input=sys.stdin.readline

dr=[(1,0),(0,1),(-1,0),(0,-1)]
cnt=1
while True:
    N=int(input())
    if N==0:
        break
    arr=[]
    for i in range(N):
        arr.append(list(map(int,input().split())))
    check=[[inf for _ in range(N)] for _ in range(N)]
    check[0][0]=arr[0][0]
    dq=deque()
    dq.append([0,0])
    result=arr[0][0]
    while dq:
        x,y=dq.popleft()
        for i,j in dr:
            mx,my=x+i,y+j
            if 0<=mx<N and 0<=my<N:
                if check[mx][my]<check[x][y]:
                    continue
                if arr[mx][my]+check[x][y]<check[mx][my]:
                    check[mx][my]=check[x][y]+arr[mx][my]
                    dq.append([mx,my])
    print('Problem %d: %d' %(cnt,check[N-1][N-1]))
    cnt+=1