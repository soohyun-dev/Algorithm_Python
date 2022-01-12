T=int(input())
for i in range(T):
  A,B=map(int,input().split())
  if A==1 or B==1:
    print(A*B)
  elif A%B==0:
    print(A)
  elif B%A==0:
    print(B)
  else:
    for i in range(2,A+1):
      if A%i==0:
        min=i*B
        if min%A==0:
          print(min)
          break

  


