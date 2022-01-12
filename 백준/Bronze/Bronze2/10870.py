N=int(input())
a=0
b=1
sum=0
if N!=1:
  for i in range(N-1):
    sum=a+b
    a=b
    b=sum
else: 
  sum=1
print(sum)
