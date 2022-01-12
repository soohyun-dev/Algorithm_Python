for i in range(int(input())):
  T=str(input())
  sum=0
  p=1
  for j in range(len(T)):
    if T[j]=='O':
      sum+=p
      p+=1
    else:
      p=1
  print(sum)

