from re import L


h,w=map(int,input().split())
place=[[0]*w for _ in range(h)]
n=int(input())
for i in range(n):
    I,d,x,y=map(int,input().split())
    if d==0:
        for j in range(I):
            place[x-1][y-1+j]=1
    elif d==1:
        for j in range(I):
            place[x-1+j][y-1]=1
            
for k in range(h):
    print(*place[k])