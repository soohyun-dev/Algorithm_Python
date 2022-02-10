import sys
input=sys.stdin.readline

N=int(input())
paper=[list(map(int,input().split())) for _ in range(N)]
cnt=[]
v=N//3

def count(x,y,num):
    for i in range(x-1):
        for j in range(y-1):
            if paper[x][y]!=paper[x+1][y+1]:
                return 

