s=0
a=0
sum=0
for i in range(1,6):
  p = list(map(int,input().split()))
  for j in range(4):
    sum+=p[j]
  if(sum>s):
    s=sum
    a=i
  sum=0
print(a, s)

