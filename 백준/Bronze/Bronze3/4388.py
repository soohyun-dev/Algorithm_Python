while(True):
  sum=0
  a,b = map(int,input().split())
  if(a==0 and b==0):
    break

  if (a%10)+(b%10) > 9:
    sum+=1
    if ((a%100)//10)+((b%100)//10) > 8:
      sum+=1
      if (a//100)+(b//100)>8:
        sum+=1
    else:
      if (a//100)+(b//100)>9:
        sum+=1
        
  else:
    if ((a%100)//10)+((b%100)//10) > 9:
      sum+=1
      if (a//100)+(b//100)>8:
        sum+=1
    else:
      if (a//100)+(b//100)>9:
        sum+=1
  print(sum)

