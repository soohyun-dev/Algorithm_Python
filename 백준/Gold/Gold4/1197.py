import heapq
import sys
input=sys.stdin.readline

V,E=map(int,input().split())
graph=[[] for _ in range(V+1)]
visited=[False]*(V+1)
visited[0],visited[1]=True,True
for i in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
result=0
C=graph[1]
heapq.heapify(C)
while C:
    Z,X=heapq.heappop(C)
    if not visited[X]:
        visited[X]=True
        result+=Z
        for i in graph[X]:
            if not visited[i[1]]:
                heapq.heappush(C,i)

print(result)
    
    