import heapq
from re import L
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
cost=[0]
for i in range(N):
    cost.append(int(input()))

graph=[[] for _ in range(N+1)]

for j in range(1,N+1):
    graph[0].append((cost[j],j))

for i in range(M):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

visited=[[False,0] for _ in range(N+1)]
q=graph[0]
heapq.heapify(q)
result=0
print(graph)
while q:
    print(q)
    Z,X=heapq.heappop(q)
    if not visited[X][0]:
        visited[X][1]+=1
        if visited[X][1]==2:
            visited[X][0]=True
        result+=Z+cost[X]
        print(Z)
        for i in graph[X]:
            if not visited[i[1]][0]:
                heapq.heappush(q,i)
print(visited)
                
print(result)