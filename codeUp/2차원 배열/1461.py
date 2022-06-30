N=int(input())
cnt=N
for i in range(1,N+1):
    for j in range(N,0,-1):
        print(cnt, end=' ')
        cnt-=1
    print()
    cnt=N*(i+1)
        