sum=0
for i in range(int(input())):
  num1,num2=map(int,input().split())
  sum+=num2%num1
print(sum)

