n,m=map(int,input().split())
for i in range(n,0,-1):
    cnt=i*m
    for j in range(m):
        print(cnt, end=' ')
        cnt-=1
    print()