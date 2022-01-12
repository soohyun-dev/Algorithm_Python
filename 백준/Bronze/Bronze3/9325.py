for i in range(int(input())):
  s=int(input())
  n=int(input())
  sum=0
  for j in range(n):
    p,q=map(int,input().split())
    sum+=p*q
  print(sum+s)
  
  