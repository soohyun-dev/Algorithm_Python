for i in range(int(input())):
  l=list(map(int,input().split()))
  sum=0
  for j in range(len(l)):
    sum+=l[j]
  print(sum)