num1,num2=map(int, input().split())
if(num1%4==0):
  a=4
  b=num1//4
else:
  a=num1%4
  b=(num1//4)+1

if(num2%4==0):
  c=4
  d=num2//4
else:
  c=num2%4
  d=(num2//4)+1

x=max(a,c)-min(a,c)
y=max(b,d)-min(b,d)
print(x+y)

