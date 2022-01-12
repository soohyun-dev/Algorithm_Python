R,B=map(int,input().split())
Square=R+B
for Row in range(3,Square+1):
  col=Square//Row
  x=Row-2
  y=x*(col-2)
  if Square-y==R and y==B:
    a=Row 
    b=col
print(a,b)



