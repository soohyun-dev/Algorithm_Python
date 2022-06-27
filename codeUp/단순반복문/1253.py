n1, n2=map(int,input().split())
a=min(n1,n2)
b=max(n1,n2)
for i in range(a,b+1):
    print(i, end=' ')