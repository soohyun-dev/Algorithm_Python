n,m=map(int,input().split())
cnt=1
for i in range(1,n+1):
    cnt=i
    for j in range(m):
        print(cnt,end=' ')
        cnt+=n
    print()