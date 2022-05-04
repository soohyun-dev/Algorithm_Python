import sys
input=sys.stdin.readline

N,M=map(int,input().split())
cloud=[]

for _ in range(N):
    cloud.append(list(input().rstrip()))

for i in range(N):
    v=-1
    check=False
    for j in range(M):
        if check==False and cloud[i][j]=='.':
            cloud[i][j]=v
        elif cloud[i][j]=='c':
            cloud[i][j]=0
            check=True
            v=1
        elif cloud[i][j]=='.':
            cloud[i][j]=v
            v+=1

for i in range(N):
    print(*cloud[i])
