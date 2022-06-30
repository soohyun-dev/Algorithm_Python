place=[]
for i in range(19):
    place.append(list(map(int,input().split())))
N=int(input())
for _ in range(N):
    x,y=map(int,input().split())
    for i in range(19):
        if place[x-1][i]==0:
            place[x-1][i]=1
        elif place[x-1][i]==1:
            place[x-1][i]=0
        if place[i][y-1]==0:
            place[i][y-1]=1
        elif place[i][y-1]==1:
            place[i][y-1]=0
for j in range(19):
    print(*place[j])