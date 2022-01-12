while(True):
  T=list(map(int,input().split()))
  if(T==[0,0,0]):
    break
  T.sort()
  if(T[2]**2 == (T[0]**2)+(T[1]**2)):
    print('right')
  else:
    print('wrong')

    