n,m=map(int,input().split())
if n%2!=0:
    cnt=((n*m)-m+1)
else:
    cnt=n*m
    
for i in range(n,0,-1):
    for j in range(m):
        print(cnt, end=' ')
        if j!=m-1:
            if i%2==0:
                cnt-=1
            else:
                cnt+=1
    cnt-=m
    print()