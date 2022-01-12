x=int(input())
while(True):
  b=input()
  if(b=='='):
    break
  a=int(input())
  if(b=='+'):
    x=x+a
  elif(b=='-'):
    x=x-a
  elif(b=='*'):
    x=x*a
  elif(b=='/'):
    x=int(x/a)
print(x)


