Q1=0
Q2=0
Q3=0
Q4=0
AXIS=0
for i in range(int(input())):
  x,y = map(int,input().split())
  if(x>0 and y>0):
    Q1+=1
  elif(x<0 and y>0):
    Q2+=1
  elif(x<0 and y<0):
    Q3+=1
  elif(x>0 and y<0):
    Q4+=1
  else:
    AXIS+=1
print('Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d' %(Q1,Q2,Q3,Q4,AXIS))



