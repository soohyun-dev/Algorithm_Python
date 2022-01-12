while True:
  N=str(input())
  if N == '0' :
    break
  while len(str(N))!=1:
    sum=0
    N=list(str(N))
    for i in range(len(N)):
      sum+=int(N[i])
    N=sum
  print(N)
