import sys
input=sys.stdin.readline
import heapq

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[True,True]+[False]*(N-1)
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
q=graph[1]
heapq.heapify(q)
result=0

tmp=0
while q:
    Z,X=heapq.heappop(q)
    if not visited[X]:
        visited[X]=True
        tmp=max(tmp,Z)
        result+=Z
        for i in graph[X]:
            if not visited[i[1]]:
                heapq.heappush(q,i)

print(result-tmp)