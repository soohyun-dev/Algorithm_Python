n=int(input())
l=list(map(int,input().split()))
M=max(l)
sum=0
for i in range(n):
  sum+=l[i]/M*100
print(sum/n)