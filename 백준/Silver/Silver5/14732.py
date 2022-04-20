import sys
input=sys.stdin.readline

N=int(input())
max_x=0
min_x=500
max_y=0
min_y=500
for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    min_x=min(min_x,x1)
    min_y=min(min_y,y1)
    max_x=max(max_x,x2)
    max_y=max(max_y,y2)

x=max_x-min_x
y=max_y-min_y

print(x*y)