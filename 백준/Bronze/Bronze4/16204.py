N,M,K=map(int,input().split())

fx=N-M
bx=N-K

if (fx>bx):
  A=bx
  print(M+A)
else:
  A=fx
  print(K+A)


