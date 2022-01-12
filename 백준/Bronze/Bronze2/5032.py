e,f,c=map(int,input().split())
sum=e+f
total=0
while sum>=c:
  total+=sum//c
  sum=sum//c + sum%c
print(total)