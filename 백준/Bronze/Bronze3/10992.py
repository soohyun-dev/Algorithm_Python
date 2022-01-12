N=int(input())
a=1
while(a<N):
  if(a==1):
    print(' '*(N-a)+'*')
    a+=1
  else:
    print(' '*(N-a)+'*'+' '*(2*a-3)+'*')
    a+=1
if(a==N):
  print('*'*(2*N-1))

  