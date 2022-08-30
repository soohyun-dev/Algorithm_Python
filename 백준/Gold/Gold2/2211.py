from cmath import inf
import heapq
from ntpath import join
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b,a))
    graph[b].append((c,a,b))
    
q=[(0,1,0)]
dist=[inf]*(N+1)
dist[1]=0
result=[0]*(N+1)

while q:
    Z,X,Y=heapq.heappop(q)
    if dist[X]<Z:
        continue
    for cost,next,now in graph[X]:
        cost+=Z
        if cost<dist[next]:
            dist[next]=cost
            result[next]=now
            heapq.heappush(q,[cost,next,now])
            
cnt=0
for i in range(2,N+1):
    if result[i]!=0:
        cnt+=1

print(cnt)
for j in range(2,N+1):
    if result[j]!=0:
        print(j,result[j])