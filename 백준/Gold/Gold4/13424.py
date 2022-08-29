from cmath import inf
import heapq
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N,M=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for i in range(M):
        a,b,c=map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))
        
    f_cnt=int(input())
    friends=list(map(int,input().split()))
    answer=0
    MIN=inf
    
    for j in range(1,N+1):
        q=[(0,j)]
        dist=[inf] * (N+1)
        dist[j]=0
        SUM=0
        while q:
            Z,X=heapq.heappop(q)
            if dist[X]<Z:
                continue
            for cost,next in graph[X]:
                cost=Z+cost
                if cost<dist[next]:
                    dist[next]=cost
                    heapq.heappush(q,[cost,next])
        for k in range(f_cnt):
            SUM+=dist[friends[k]]
            
        if MIN>SUM:
            MIN=SUM
            answer=j
    print(answer)
            