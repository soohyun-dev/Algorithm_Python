A,B = map(int,input().split())
C,D = map(int,input().split())

sum1=(A/C)+(B/D)
sum2=(C/D)+(A/B)
sum3=(D/B)+(C/A)
sum4=(B/A)+(D/C)

m=max(sum1,sum2,sum3,sum4)
l=[sum1,sum2,sum3,sum4]
a=0

for i in range(4):
  if(l[i]==m):
    a+=1
if(a==1):
  if(m==sum1):
    print(0)
  elif(m==sum2):
    print(1)
  elif(m==sum3):
    print(2)
  else:
    print(3)

else:
  m=min(sum1,sum2,sum3,sum4)
  if(m==sum1):
    print(0)
  elif(m==sum2):
    print(1)
  elif(m==sum3):
    print(2)
  else:
    print(3)

  
