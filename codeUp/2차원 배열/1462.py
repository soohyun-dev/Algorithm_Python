N=int(input())

for i in range(1,N+1):
    cnt=i
    for j in range(N):
        print(cnt, end=' ')
        cnt+=N
    print()