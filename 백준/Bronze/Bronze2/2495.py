for i in range(3):
  N=list(input())
  cnt=1
  M=1
  for j in range(1,len(N)):
    if N[j-1]==N[j]:
      cnt+=1
      if M<cnt:
        M=cnt
    else:
      cnt=1
  print(M)

