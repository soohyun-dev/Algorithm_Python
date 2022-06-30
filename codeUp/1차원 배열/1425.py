N,C=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for i in range(N):
    if (i+1)%C==0:
        print(l[i])
    else:
        print(l[i],end=' ')
    