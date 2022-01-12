N=int(input())
hill=list(map(int,input().split()))
sum=0
cnt=0
maxH=0

for i in hill:
  if i > maxH:
    maxH = i
    cnt=0
  else:
    cnt+=1
  sum=max(sum,cnt)
print(sum)
