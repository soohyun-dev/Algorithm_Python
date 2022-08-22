import heapq

N=int(input())
matrix=[]
for i in range(N):
    matrix.append(list(map(int,input().split())))

graph=[[] for _ in range(N)]
visited=[True]+[False]*(N-1)

for i in range(N):
    for j in range(i+1,N):
        graph[i].append((matrix[i][j],j))
        graph[j].append((matrix[i][j],i))

q=graph[0]
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