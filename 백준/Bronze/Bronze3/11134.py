for i in range(int(input())):
  N,C=map(int,input().split())
  if(N%C==0):
    print(N//C)
  else:
    print(N//C+1)