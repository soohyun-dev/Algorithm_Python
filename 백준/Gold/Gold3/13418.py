import heapq
import sys
input = sys.stdin.readline

def MST(graph):
    visited=[True]+[False]*(N)
    q=graph[0]
    heapq.heapify(q)
    result=0
    while q:
        Z,X=heapq.heappop(q)
        if not visited[X]:
            visited[X]=True
            result+=Z
            for j in graph[X]:
                if not visited[j[1]]:
                    heapq.heappush(q,j)
    print(result)
    return result

N,M=map(int,input().split())
max_graph=[[] for _ in range(N+1)]
min_graph=[[] for _ in range(N+1)]
for i in range(M+1):
    a,b,c=map(int,input().split())
    if c==0:
        max_graph[a].append((0,b))
        max_graph[b].append((0,a))
        min_graph[a].append((1,b))
        min_graph[b].append((1,a))
    else:
        max_graph[a].append((1,b))
        max_graph[b].append((1,a))
        min_graph[a].append((0,b))
        min_graph[b].append((0,a))

print(max_graph)
print(min_graph)

MAX=(N-MST(max_graph))**2
MIN=MST(min_graph)**2
print(MAX,MIN)