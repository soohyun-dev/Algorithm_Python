N=int(input())
for i in range(N,0,-1):
    cnt=i
    for j in range(N):
        print(cnt, end=' ')
        cnt+=N
    print()