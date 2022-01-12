L,P=map(int,input().split())
A=L*P
n=list(map(int, input().split()))
for i in n:
  print(i-A,end=' ')

