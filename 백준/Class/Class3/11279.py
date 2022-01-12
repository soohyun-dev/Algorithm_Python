import sys
import heapq

heap=[]
N=int(input())
for i in range(N):
  a=int(sys.stdin.readline())
  if a == 0:
    if heap:
      print(-heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap, -a)

