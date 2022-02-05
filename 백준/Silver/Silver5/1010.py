import sys
input=sys.stdin.readline
for _ in range(int(input())):

    n,m=map(int,input().split())

    if n==0 or n==m:
        print(1)
    elif n==1 or n==(m-1):
        print(m)
    else:
        if m//2 < n:
            n=m-n
        left=m
        right=n

        for i in range(n-1):
            m=m-1
            left*=m
        for j in range(n-1):
            n=n-1
            right*=n

        print(left//right)