import sys
input=sys.stdin.readline

N,M=map(int,input().split())
Trees=list(map(int,input().split()))

low, high = 0, max(Trees)

while low <= high:
  cut=(low+high)//2
  sum=0

  for tree in Trees:
    if tree>cut:
      sum+=tree-cut    

  if sum >= M:
    low=cut+1
  else:
    high=cut-1


print(high)



