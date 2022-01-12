N,L,D = map(int,input().split())
T=L+5
if(T>D and L<D):
  print(D)
elif(D<L):
  print(((L//D)+1)*D)
  #D가 6보다 큰경우 고려
else:
  if(T%D==0):
    c=L*N+((N-1)*5)+D+1
    print(c)  
  else:
    a=D//T
    if(a==1):
      b=1
      while(D*b>(T+(T)*b)):
        b+=1
      print(D*b)
    else:
      print(a*D)


 