for i in range(int(input())):
  sum=0
  num=int(input())
  l=list(map(int,input().split()))
  for j in range(num):
    sum+=l[j]
  print(sum)


