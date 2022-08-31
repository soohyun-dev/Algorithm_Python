from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
u,v=map(int,input().split())
check=[1,u,v]
result_1=0
result_2=0
for i in range(3):
    q=[(0,check[i])]
    dist=[inf]*(N+1)
    dist[check[i]]=0
    while q:
        Z,X=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next in graph[X]:
            cost=cost+Z
            if dist[next]>cost:
                dist[next]=cost
                heapq.heappush(q,[cost,next])
    if i==0:
        result_1+=dist[u]
        result_2+=dist[v]
    elif i==1:
        result_1+=dist[v]
        result_2+=dist[N]
    elif i==2:
        result_1+=dist[N]
        result_2+=dist[u]

answer=min(result_1,result_2)
if answer==inf:
    print(-1)
else:
    print(answer)