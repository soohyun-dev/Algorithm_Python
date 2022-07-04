n,m=map(int,input().split())
check=[[] for _ in range(n)]
cnt=1
for i in range(1,n+1): 
    for j in range(i-1,-1,-1):
        check[n-j-1].append(cnt)
        cnt+=1
        
tmp=n*m
for k in range(2,n):
    tmp-=k
    
while tmp>cnt:
    for i in range(n):
        check[i].append(cnt)
        cnt+=1

for i in range(1,n+1):
    for j in range(n-i):
        if cnt>n*m:
            break
        check[j].append(cnt)
        cnt+=1

for k in range(n):
    check[k].reverse()
    print(*check[k], end=" ")
    print()