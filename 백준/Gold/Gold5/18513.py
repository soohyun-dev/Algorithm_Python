from collections import deque
import sys
input=sys.stdin.readline

def bfs():
  queue=deque()
  visited=set()
  cnt=0
  sum=0
  for i in sam:
    queue.append((i,1))  
    visited.add(i)
  while queue:
    place, unlucky=queue.popleft() 
    for check in [place+1, place-1]:
      if check not in visited:
        visited.add(check)
        queue.append((check, unlucky+1))
        sum+=unlucky
        cnt+=1
        if cnt==K:
          queue=list()
          break
  print(sum)

N,K=map(int,input().split())
sam=list(map(int,input().split()))

bfs()


