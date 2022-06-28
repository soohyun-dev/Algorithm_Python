n,k=map(int,input().split())

if k==0:
    print(1)
else:
    t=n
    for i in range(k-1):
        n*=t
    print(n)