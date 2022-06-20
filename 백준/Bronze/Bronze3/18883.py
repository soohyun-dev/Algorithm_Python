N,M=map(int,input().split())
cnt=1
for i in range(N):
    for j in range(M):
        if j!=M-1:
            print(cnt, end=' ')
        else:
            print(cnt)
        cnt+=1
