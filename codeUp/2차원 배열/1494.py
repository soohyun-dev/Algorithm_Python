n,k=map(int,input().split())
A=[0]*n
for i in range(k):
    s,e,u=map(int,input().split())
    A[s-1]+=u
    A[e]-=u
print(*A,end=' ')
print()
tmp=0
for i in range(1,n):
    A[i]=A[i]+A[i-1]

print(*A,end=' ')