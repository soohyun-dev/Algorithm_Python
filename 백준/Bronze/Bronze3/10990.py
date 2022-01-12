N=int(input())
a=0
for i in range(1,N+1):
  print(' '*(N-i)+'*'+' '*(2*i-3)+'*'*a)
  a=1