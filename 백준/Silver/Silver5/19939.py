N,K=map(int,input().split())
tmp=N//K
check=[tmp]*K

cnt=0
for i in range(1,K+1):
    if i%2==0:
        check[i-1]+=cnt
    else:
        check[i-1]-=cnt
        cnt+=1
        
check.sort()

if sum(check)>N:
    tmp=sum(check)-N
    check[tmp-1]-=tmp
elif sum(check)<N:
    tmp=N-sum(check)
    check[K-tmp]+=tmp
    
a=max(check)
b=min(check)

if b<1 or sum(check)!=N:
    print(-1)
else:
    print(a-b)
    
    
    