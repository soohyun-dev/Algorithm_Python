n,m=map(int,input().split())
check=[[] for _ in range(n)]
if m%2==0:
    cnt=n*m-(n-1)
else:
    cnt=n*m
for i in range(m):
    for j in range(n):
        check[j].append(cnt)
        if (m-i)%2!=0 and j!=n-1:
            cnt-=1
        elif (m-i)%2==0 and j!=n-1:
            cnt+=1
    cnt-=n
        
    
for k in range(n):
    print(*check[k], end=' ')
    print()