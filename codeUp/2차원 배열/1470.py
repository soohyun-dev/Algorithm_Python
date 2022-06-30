n=int(input())
check=[[] for _ in range(n)]
cnt=1
for i in range(n):
    if i%2==0:
        for j in range(n):
            check[j].append(cnt)
            if j!=n-1:
               cnt+=1
    else:
        for j in range(n):
            check[j].append(cnt)
            if j!=n-1:
                   cnt-=1
    cnt+=n

for k in range(n):
    print(*check[k],end=' ')
    print()        