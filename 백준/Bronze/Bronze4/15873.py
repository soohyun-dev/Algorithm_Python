num=int(input())
if(num>110 and num!=1010):   # B 에 10이 오는경우
  a=num//100
  b=num-(a*100)
  print(a+b)
elif(num==1010): # 1000이 넘어가는 경우는 둘다 10일경우밖에 없다.
  print(20)
else:            # 109이하의 경우
  a=num//10
  b=num%10
  print(a+b)


