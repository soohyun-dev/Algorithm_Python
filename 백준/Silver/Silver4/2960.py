N,K=map(int,input().split())
cnt=0
l=list([i for i in range(2, N+1)])

while True:
    if cnt==K:
        break
    if min(l)!=0:
        m=min(l)
        l.remove(min(l))
        cnt+=1
        if cnt==K:
            print(m)
            break
        else:
            tmp=2
            value=m
            while m<=N:
                m=value*tmp
                if m in l:
                    l.remove(m)
                    cnt+=1
                if cnt==K:
                    print(m)
                    break
                tmp+=1




