from cmath import inf
import heapq
import sys
input=sys.stdin.readline

n,m,r=map(int,input().split())
arr=[0]+list(map(int,input().split()))
graph=[[] for _ in range(n+1)]

for i in range(r):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

MAX=0
for i in range(1,n+1):
    dist=[inf]*(n+1)
    q=[(i,0)]
    dist[i]=0
    result=arr[i]
    while q:
        node,cost=heapq.heappop(q)
        if dist[node]<cost:
            continue
        for C,next in graph[node]:
            tmp=C+cost
            if tmp<=m:
                if tmp<=dist[next]:
                    dist[next]=tmp
                    result+=arr[next]
                    heapq.heappush(q,[next,tmp])
    SUM=0
    print(dist)
    for j in range(1,n+1):
        if dist[j]<=m:
            SUM+=arr[j]
    if MAX<SUM:
        MAX=SUM
                        
print(MAX)
            
        