n,m=map(int,input().split())
for i in range(n):
    cnt=(n*m)-i
    for i in range(m):
        print(cnt, end=' ')
        cnt-=n
    print()