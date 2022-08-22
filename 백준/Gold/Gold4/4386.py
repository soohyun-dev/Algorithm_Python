import heapq
import sys
input=sys.stdin.readline

N=int(input())
stars=[[] for _ in range(N+1)]
graph=[[] for _ in range(N+1)]
visited=[True,True]+[False]*(N-1)
for i in range(N):
    stars[i+1]=(list(map(float,input().split())))
for i in range(1,N):
    for j in range(i+1,N+1):
        tmp=((stars[i][0]-stars[j][0])**2+(stars[i][1]-stars[j][1])**2)**(1/2)
        graph[i].append((tmp,j))
        graph[j].append((tmp,i))

q=graph[1]
heapq.heapify(q)
result=0
while q:
    Z,X=heapq.heappop(q)
    if not visited[X]:
        visited[X]=True
        result+=Z
        for i in graph[X]:
            if not visited[i[1]]:
                heapq.heappush(q,i)
    
print(round(result,2))