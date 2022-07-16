a,b=map(int,input().split())
result=[]
for j in range(2):
    if j==1:
        N=b+2
    else:
        N=a+1
    center=N//2
    tmp=N
    l=[]
    cnt=0
    while tmp>1:
        tmp//=2
        l.append(tmp+1)
        for i in range(2):
            if tmp-i<=1:
                break
            l.append(tmp-i)
        cnt+=1
    l.sort()
    l.append(N)

    fibo={}
    fibo[0]=0
    fibo[1]=1
    fibo[2]=1

    for i in l:
        cnt-=1
        a=i//2
        if i%2==0: 
            fibo[i]=((2*fibo[a-1]+fibo[a])*fibo[a])%1000000000000000000
        else:
            fibo[i]=((fibo[a+1]**2)+(fibo[a]**2))%1000000000000000000
        if i==N:
            break
    
    result.append(fibo[N]-1)
print(abs(result[1]-result[0])%1000000000)
