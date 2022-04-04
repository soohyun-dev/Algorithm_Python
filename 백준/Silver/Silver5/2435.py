N,K=map(int,input().split())
tem=list(map(int,input().split()))
top=-100
for i in range(N-K+1):
    top=max(sum(tem[i:K+i]),top)

print(top)


