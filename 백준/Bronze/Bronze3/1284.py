a=0
sum=0
while(a==0):
  n = int(input())
  nl=list(map(int, str(n)))
  if(n>=1000):
    for i in range(4):
      if (nl[i]==1):
        sum+=2
      elif(nl[i]==0):
        sum+=4
      else:
        sum+=3
    print(sum+5)
    sum=0
  elif(n>=100):
    for i in range(3):
      if (nl[i]==1):
        sum+=2
      elif(nl[i]==0):
        sum+=4
      else:
        sum+=3
    print(sum+4)
    sum=0
  elif(n>=10):
    for i in range(2):
      if (nl[i]==1):
        sum+=2
      elif(nl[i]==0):
        sum+=4
      else:
        sum+=3
    print(sum+3)
    sum=0
  elif(n<10 and n>0):
    if (n==1):
        sum+=2
    elif(n==0):
        sum+=4
    else:
        sum+=3
    print(sum+2)
    sum=0
  else:
    a=1

  

