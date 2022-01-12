num=int(input())
if(num%2!=0):  # 홀수
  print(0)
else:
  if((num//2)%2==0): # 2로 나누었을때 짝수
    print(2)
  else:              # 2로 나누었을때 홀수
    print(1)

    