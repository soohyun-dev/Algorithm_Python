import sys

for i in range(3):
  sum=0
  num=int(sys.stdin.readline())
  for j in range(num):
    sum+=int(sys.stdin.readline())
  if (sum>0):
    print('+')
  elif(sum<0):
    print('-')
  else:
    print(0)



    
