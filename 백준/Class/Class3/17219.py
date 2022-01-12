import sys

N,M=map(int,input().split())
l={}
for i in range(N):
  web_add,pwd=sys.stdin.readline().split()
  l[web_add]=pwd
for j in range(M):
  print(l[input()])


  