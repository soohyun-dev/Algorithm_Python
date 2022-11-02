import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
order=[[] for _ in range(N+1)]
rank=[0 for _ in range(N+1)]
queue=[]
result=[]
for i in range(M):
    front,back=map(int,input().split())
    rank[back]+=1
    order[front].append(back)
    
for j in range(1,N+1):
    if rank[j]==0:
        heapq.heappush(queue,j)

while queue:
    nowProblem=heapq.heappop(queue)
    result.append(nowProblem)
    for nextProblem in order[nowProblem]:
        rank[nextProblem]-=1
        if rank[nextProblem]==0:
            heapq.heappush(queue, nextProblem)
            
print(' '.join(map(str,result)))
            
            