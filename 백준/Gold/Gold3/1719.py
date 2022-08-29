from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b,a))
    graph[b].append((c,a,b))

matrix=[]
for j in range(1,N+1):
    q=[(0,j)]
    dist=[inf]*(N+1)
    chart=[0]*(N+1)
    dist[j]=0
    while q:
        Z,X=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next,now in graph[X]:
            cost=cost+Z
            if cost<dist[next]:
                dist[next]=cost
                chart[next]=now
                heapq.heappush(q,[cost,next])
    matrix.append(chart)
    
for i in range(1,N+1):
    for j in range(N):
        if i-1==j:
            print('-', end=' ')
        else:
            print(matrix[j][i],end=' ')
    print()