N,M=map(int,input().split())
cnt=N
while True:
    tmp=N//M
    if tmp<M:
        cnt+=tmp
        print(cnt)
        break
    else:
        cnt+=tmp
        N=tmp
        