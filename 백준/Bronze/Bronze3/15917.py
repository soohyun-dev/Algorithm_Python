import sys

N=int(input())
for i in range(N):
  a = int(sys.stdin.readline())
  if a&(-a) == a:
    print(1)
  else:
    print(0)