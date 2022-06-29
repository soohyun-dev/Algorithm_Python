N=int(input())
check=[False]*(N+1)
for i in range(N-1):
    num=int(input())
    check[num]=True

for i in range(1,N+1):
    if check[i]==False:
        print(i)
        break