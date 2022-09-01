from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N,M,start,end,money=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b,a,c))
    graph[b].append((c,a,b,c))
    
dist=[inf]*(N+1)
dist[start]=0
q=[(0,start,0,0)]
arr=[[0,0] for _ in range(N+1)]
while q:
    Z,X,Y,T=heapq.heappop(q)
    if dist[X]<Z:
        continue
    for cost,next,now,pay in graph[X]:
        cost+=Z
        if cost<dist[next]:
            dist[next]=cost
            arr[next][0]=now
            arr[next][1]=pay
            heapq.heappush(q,[cost,next,now,pay])

if dist[end]<money:
    MAX=0
    while start!=end:
        if MAX<arr[end][1]:
            MAX=arr[end][1]
        end=arr[end][0]
    print(MAX)   
else:
    print(-1)