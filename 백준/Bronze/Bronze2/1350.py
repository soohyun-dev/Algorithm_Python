N=int(input())
l=list(map(int,input().split()))
C=int(input())
tmp=0
for i in range(N):
    if l[i]%C==0:
        tmp+=l[i]//C
    else:
        tmp+=(l[i]//C)+1
print(tmp*C)