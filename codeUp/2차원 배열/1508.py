N=int(input())
check=[[] for _ in range(N)]
for i in range(N):
    check[i].append(int(input()))
for i in range(N):
    for j in range(i):
        check[i].append(check[i][j]-check[i-1][j])
        
for i in range(N):
    print(*check[i], end=' ')
    print()