num1,num2=map(int,input().split())

if((num1 and num2)<0 and (num1%num2!=0)):
  a=(abs(num1)//abs(num2))+1
  print(a)
  print(num1+abs(a*num2))

else:
  print(num1//num2)
  print(abs(num1%num2))