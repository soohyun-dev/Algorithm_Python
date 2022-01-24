import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

for i in range(1,N):
  l[i][0]=min(l[i-1][1], l[i-1][2])+l[i][0];
  l[i][1]=min(l[i-1][0], l[i-1][2])+l[i][1];
  l[i][2]=min(l[i-1][0], l[i-1][1])+l[i][2];

print(min(l[N-1]))