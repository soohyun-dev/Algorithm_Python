import sys
input=sys.stdin.readline

a=[]
b=[]
N,M=map(int,input().split())
for i in range(N):
    road, speed=map(int,input().split())
    for j in range(road):
        a.append(speed)

for i in range(M):
    road, speed=map(int,input().split())
    for j in range(road):
        b.append(speed)
        
tmp=0

for i in range(100):
    if b[i]-a[i] > tmp:
        tmp=b[i]-a[i]

print(tmp)


