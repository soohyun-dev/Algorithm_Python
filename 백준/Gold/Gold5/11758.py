x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

a=x1-y1
b=x2-y2
c=x3-y3

if a==0 and b==0 and c==0:
  print(0)
elif a==0 and b==0 and c>0 :
  print(-1)
elif a==0 and b>0 and c==0:
  print(1)