num=int(input())
l = list(map(int,input().split()))
sum=0
for i in range(num):
  n=l[i]*(i+1)-sum
  print(n, end=' ')
  sum+=n

