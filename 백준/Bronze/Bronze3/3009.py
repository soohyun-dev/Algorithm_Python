x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
if(x1==x2):
  a=x3
elif(x1==x3):
  a=x2
else:
  a=x1
if(y1==y2):
  b=y3
elif(y1==y3):
  b=y2
else:
  b=y1
print(a, b)

