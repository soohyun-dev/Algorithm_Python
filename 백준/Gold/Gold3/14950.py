import heapq
import sys
input=sys.stdin.readline

N,M,T=map(int,input().split())
city=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    city[a].append((c,b))
    city[b].append((c,a))

visited=[True,True]+[False]*(N-1)
q=city[1]
heapq.heapify(q)
result=0

cnt=0
while q:
    Z,X=heapq.heappop(q)
    if not visited[X]:
        visited[X]=True
        result+=Z+(T*cnt)

        for i in city[X]:
            if not visited[i[1]]:
                heapq.heappush(q,i)
        cnt+=1
                
print(result)