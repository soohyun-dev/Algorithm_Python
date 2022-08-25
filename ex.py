import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N,M=map(int,input().split())
    arr=[]
    for i in range(N):
        l=map(int,input().split())
        for j in l:
            arr.append(j)
    for i in range(N-1):
        l=map(int,input().split())
        for j in l:
            arr.append(j)
    arr.sort()
    sum=0
    cnt=N*M-1
    for i in range(cnt):
        sum+=arr[i]
    print(sum)