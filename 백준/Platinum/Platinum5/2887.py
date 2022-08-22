import heapq
import sys
input=sys.stdin.readline

N=int(input())
planets=[[] for _ in range(N+1)]
for i in range(1,N+1):
    planets[i]=list(map(int,input().split()))
    planets[i]+=[i]
planets[0]=[sys.maxsize,sys.maxsize,sys.maxsize,0]
    
visited=[True,True]+[False]*(N-1)
graph=[[] for _ in range(N+1)]

for i in range(3):
    planets.sort(key=lambda x:x[i])
    for j in range(1,N):
        a,b,c,d=planets[j-1]
        A,B,C,D=planets[j]
        graph[d].append((min(abs(a-A),abs(b-B),abs(c-C)),D))
        graph[D].append((min(abs(a-A),abs(b-B),abs(c-C)),d))
    
q=graph[1]
heapq.heapify(q)
result=0

while q:
    Z,X=heapq.heappop(q)
    if not visited[X]:
        result+=Z
        visited[X]=True
        for i in graph[X]:
            if not visited[i[1]]:
                heapq.heappush(q,i)

print(result)