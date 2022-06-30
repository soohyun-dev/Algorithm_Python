N=int(input())
place=[[0]*19 for i in range(19)]
for i in range(N):
    x,y=map(int,input().split())
    place[x-1][y-1]=1
for j in range(19):
    print(*place[j])