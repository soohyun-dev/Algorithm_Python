n,m=map(int,input().split())
check=[[]for _ in range(n)]
if m%2==0:
    cnt=n*m
else:
    cnt=(n*m)-n+1
    
for i in range(m,0,-1):
    if i%2==0:
        for j in range(n):
            check[j].append(cnt)
            if j!=n-1:
                cnt-=1
    else:
        for j in range(n):
            check[j].append(cnt)
            if j!=n-1:
                cnt+=1
    cnt-=n
for k in range(n):
    print(*check[k], end=' ')
    print()     