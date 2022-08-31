import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
school=['X']+list(input().split())
graph=[[] for _ in range(N+1)]

for i in range(M):
    u,v,d=map(int,input().split())
    if school[u]!=school[v]:
        graph[u].append((d,v))
        graph[v].append((d,u))

q=graph[1]
visited=[True]+[False]*N
visited[1]=True
cnt=0
heapq.heapify(q)
result=0
while q:
    Z,X=heapq.heappop(q)
    if not visited[X]:
        visited[X]=True
        cnt+=1
        result+=Z
        for i in graph[X]:
            if not visited[i[1]]:
                heapq.heappush(q,i)
if cnt==N-1:
    print(result)
else:
    print(-1)
