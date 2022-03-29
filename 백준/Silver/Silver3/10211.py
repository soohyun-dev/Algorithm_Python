import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    N=int(input())
    check=[0]*N
    sum=0
    X=list(map(int,input().split()))
    for i in range(N):
        sum+=X[i]
        if X[i]<=sum:
            check[i]=sum
        else:
            sum=X[i]
            check[i]=X[i]
    print(max(check))


    