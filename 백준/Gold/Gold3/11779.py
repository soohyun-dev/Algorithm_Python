from cmath import inf
import heapq
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
start,end=map(int,input().split())

near=[start]*(n+1)
dist=[inf]*(n+1)
q=[(0,start)]

while q:
    C,N=heapq.heappop(q)
    if C>dist[N]:
        continue
    for x,y in graph[N]:
        cost=C+x
        if cost<dist[y]:
            near[y]=N
            dist[y]=cost
            heapq.heappush(q,(cost,y))
            
S=end
result=[end]
while S!=start:
    I=near[S]
    result.append(I)
    S=I
result.reverse()
print(dist[end])
print(len(result))
print(*result)