import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(M):
        if j>=1:
            arr[i][j]+=arr[i][j-1]

for i in range(int(input())):
    i,j,x,y=map(int,input().split())
    sum=0
    if i==x and j==y:
        if j>1:
            print(arr[i-1][j-1]-arr[i-1][j-2])
        else:
            print(arr[i-1][j-1])
    else:
        for k in range(i-1,x):
            if j-2>=0:
                sum+=(arr[k][y-1]-arr[k][j-2])
            else:
                sum+=arr[k][y-1]
        print(sum)
        