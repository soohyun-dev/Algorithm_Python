n=int(input())
a=0
b=1
c=0
for i in range(n):
  c=b
  b=a+b
  a=c
print(a)

