while(True):
  a,b,c = map(int,input().split())
  if(a==0 and b==0 and c==0):
    break
  L=[a,b,c]
  L.sort()
  if(L[2] >= L[0]+L[1]):
    print('Invalid')
  elif(L[0]==L[1]==L[2]):
    print('Equilateral')
  elif(L[0]!=L[1]!=L[2]):
    print('Scalene')
  else:
    print('Isosceles')


    