while True:
  num1,num2=map(int,input().split())
  if(num1==0 or num2==0):
    break
  print(num1//num2, num1%num2, '/', num2)


  