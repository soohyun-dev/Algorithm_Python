import heapq
import sys
input=sys.stdin.readline

N=int(input())
heap=[]
heapq.heapify(heap)

for _ in range(N):
    tmp=list(map(int,input().split()))
    for i in range(N):
        heapq.heappush(heap, tmp[i])
        if len(heap)>N:
            heapq.heappop(heap)
            
print(heap[0])

