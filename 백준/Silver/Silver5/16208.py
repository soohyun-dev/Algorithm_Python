N=int(input())
a=sorted(list(map(int,input().split())))
tmp=sum(a)
sum=0
for i in range(N):
    tmp-=a[i]
    sum+=(a[i]*tmp)

print(sum)




