import sys
input=sys.stdin.readline

N=int(input())
max_x=0
min_x=500
max_y=0
min_y=500
block=[]
for i in range(501):
    block.append([False]*501)
cnt=0

for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    min_x=min(min_x,x1)
    min_y=min(min_y,y1)
    max_x=max(max_x,x2)
    max_y=max(max_y,y2)
    for j in range(x1,x2):
        for k in range(y1,y2):
            block[k][j]=True
            
for i in range(min_x,max_x):
    for j in range(min_y, max_y):
        if block[j][i]==True:
            cnt+=1
            
print(cnt)


