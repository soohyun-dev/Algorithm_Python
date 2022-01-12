import sys
import heapq

heap=[]
n=int(input())
for i in range(n):
  a=int(sys.stdin.readline())
  if a==0:
    if heap: # heap 에 값이 존재
      print(heapq.heappop(heap))  # 삭제 후 출력
    else:
      print(0)
  else:
    heapq.heappush(heap,a)  # heap 에 a 값 추가

