N,M=map(int,input().split())
if N!=0:
    l=list(map(int,input().split()))
cnt=0
i=0
sum=0
while i<N:
    sum+=l[i]
    if sum<M:
        i+=1
        if i==N:
            i+=1
            cnt+=1
    elif sum==M:
        cnt+=1 
        i+=1
        sum=0
    else:
        cnt+=1
        sum=0
        
print(cnt)
    
    
