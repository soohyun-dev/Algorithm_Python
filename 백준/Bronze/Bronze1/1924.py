x,y=map(int,input().split())
if x==1:
  day=0
else:
  day=31
  for i in range(1,x):
    if i==2:
      day+=28
    elif i==3 or i==5 or i==7 or i==8 or i==10:
      day+=31
    elif i==4 or i==6 or i==9 or i==11:
      day+=30
    else:
      day+=28
day+=y
if day%7==0:
  print('SUN')
elif day%7==1:
  print('MON')
elif day%7==2:
  print('TUE')
elif day%7==3:
  print('WED')
elif day%7==4:
  print('THU')
elif day%7==5:
  print('FRI')
else:
  print('SAT')

