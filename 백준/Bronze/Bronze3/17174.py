N,M=map(int,input().split())
cnt=N
while True:
    N//=M
    cnt+=N
    if N<M:
        print(cnt)
        break
        
        