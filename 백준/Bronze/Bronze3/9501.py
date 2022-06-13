for _ in range(int(input())):
    N,D=map(int,input().split())
    cnt=0
    for i in range(N):
        v,f,c=map(int,input().split())
        tmp=f/c
        result=v*tmp
        if D<=result:
            cnt+=1
    print(cnt)
    
    