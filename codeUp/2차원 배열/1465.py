n,m=map(int,input().split())
for i in range(n,0,-1):
    cnt=(i*m)
    for j in range(m-1,-1,-1):
        print(cnt-j,end=' ')
    print()
    