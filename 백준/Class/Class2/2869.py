A,B,V=map(int,input().split())
result=V-B
AB=A-B
div=result%AB
day=result//AB

if div==0:
  print(day)
else:
  print(day+1)
