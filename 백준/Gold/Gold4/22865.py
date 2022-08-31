from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N=int(input())
graph=[[] for _ in range(N+1)]
ABC=list(map(int,input().split()))
M=int(input())
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
result=[]
for j in range(3):
    q=[(0,ABC[j])]
    dist=[inf]*(N+1)
    dist[ABC[j]]=0
    while q:
        Z,X=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next in graph[X]:
            cost+=Z
            if cost<dist[next]:
                dist[next]=cost
                heapq.heappush(q,[cost,next])
    result.append(dist)

MAX=0
for i in range(1,N+1):
    if i in ABC:
        continue
    tmp=min(result[0][i],result[1][i],result[2][i])
    if MAX<tmp:
        MAX=tmp
        answer=i
print(answer)