for i in range(int(input())):
  N,M=map(int,input().split())
  leg=M*2
  cnt=leg-N
  print(cnt, M-cnt)