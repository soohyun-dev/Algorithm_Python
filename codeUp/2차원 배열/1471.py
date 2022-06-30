n=int(input())
cnt=n
check=[[] for _ in range(n)]
for i in range(n):
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
    cnt+=n
    
for k in range(n):
    print(*check[k], end=' ')
    print()