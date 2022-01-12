n=int(input())
if(n==2):
  A,B=map(int,input().split())
  for i in range(1,min(A,B)+1):
    if A%i==0 and B%i==0:
      print(i)
else:
  A,B,C=map(int,input().split())
  for j in range(1, min(A,B,C)+1):
    if A%j==0 and B%j==0 and C%j==0:
      print(j)

