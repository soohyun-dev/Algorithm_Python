import heapq
import sys
input=sys.stdin.readline

N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))
graph=[[] for i in range(N+1)]
matrix=[[]]
for i in range(N):
    graph[0].append((arr[i],i+1))
for i in range(N):
    matrix.append(list(map(int,input().split())))
    matrix[i+1]=[0]+matrix[i+1]
for i in range(1,N):
    for j in range(i+1,N+1):
        graph[i].append((matrix[i][j],j))
        graph[j].append((matrix[i][j],i))

visited=[True]+[False]*(N)
q=graph[0]
heapq.heapify(q)
result=0
cnt=0
while q:
    if cnt==N:
        break
    Z,X=heapq.heappop(q)
    if not visited[X]:
        visited[X]=True
        cnt+=1
        result+=Z
        for j in graph[X]:
            if not visited[j[1]]:
                heapq.heappush(q,j)
print(result)
