import heapq
import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
e=list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
for i in e:
    graph[0].append((0,i))
for i in range(M):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
    
visited=[True]+[False]*(N)
q=graph[0]
heapq.heapify(q)
result=0

while q:
    Z,X=heapq.heappop(q)
    if not visited[X]:
        visited[X]=True
        result+=Z
        for i in graph[X]:
            if not visited[i[1]]:
                heapq.heappush(q,i)    
            
print(result)