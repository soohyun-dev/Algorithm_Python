N=int(input())
s=[2**i for i in range(31)]
if N in s:
  print(1)
else:
  print(0)