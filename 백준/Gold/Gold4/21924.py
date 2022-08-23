import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
total=0

for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    total+=c

visited=[True,True]+[False]*(N-1)
q=graph[1]
heapq.heapify(q)
result=0
cnt=0

while q:
    Z,X=heapq.heappop(q)
    if not visited[X]:
        visited[X]=True
        result+=Z
        cnt+=1
        for i in graph[X]:
            if not visited[i[1]]:
                heapq.heappush(q,i)
                
if cnt==N-1:
    print(total-result)
else:
    print(-1)