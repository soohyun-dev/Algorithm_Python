n,m=map(int,input().split())

if m==0 or m==n:
    print(1)
elif m==1 or m==(n-1):
    print(n)
else:
    if n//2 < m:
        m=n-m
    left=n
    right=m

    for i in range(m-1):
        n=n-1
        left*=n
    for j in range(m-1):
        m=m-1
        right*=m

    print(left//right)

    