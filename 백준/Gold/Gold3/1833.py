import heapq
import sys
input=sys.stdin.readline

N=int(input())
matrix=[]
for i in range(N):
    matrix.append(list(map(int,input().split())))
    
graph=[[] for _ in range(N+1)]

total=0
for i in range(N):
    for j in range(i+1,N):
        tmp=matrix[i][j]
        if tmp<0:
            graph[i+1].append((tmp,j+1,0,i+1))
            graph[j+1].append((tmp,i+1,0,j+1))
            total+=(-tmp)
        else:
            graph[i+1].append((tmp,j+1,1,i+1))
            graph[j+1].append((tmp,i+1,1,j+1))

visited=[True,True]+[False]*(N-1)
q=graph[1]
heapq.heapify(q)
result=0
answer=[]

while q:
    print(q)
    Z,X,C,D=heapq.heappop(q)
    if not visited[X]:
        if C==1:
            result+=Z
            answer.append([D,X])
        visited[X]=True
        for i in graph[X]:
            if not visited[i[1]]:
                heapq.heappush(q,i)
print(total+result,len(answer))
for i in range(len(answer)):
    print(*answer[i])