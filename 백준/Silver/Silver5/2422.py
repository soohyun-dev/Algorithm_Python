import sys
input=sys.stdin.readline

N,M=map(int,input().split())

check=[[False for _ in range(N)] for _ in range(N)]
for i in range(M):
    front, back = map(int,input().split())
    check[front-1][back-1]=True
    check[back-1][front-1]=True

sum=0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if not check[i][j] and not check[i][k] and not check[j][k]:
                sum+=1

print(sum)