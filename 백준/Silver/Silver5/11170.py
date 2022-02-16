for i in range(int(input())):
    N,M=(map(int,input().split()))
    cnt=0
    for i in range(N,M+1):
        l=list(str(i))
        for j in range(len(l)):
            if l[j]=='0':
                cnt+=1
    print(cnt)


