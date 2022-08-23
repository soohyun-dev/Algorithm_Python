import heapq
import copy
import sys
input=sys.stdin.readline
    
def MST(a,graph):
    visited=[True,True]+[False]*(N-1)
    tmp=copy.deepcopy(graph)
    q=tmp[1]
    heapq.heapify(q)
    result=0
    cnt=0
    while q:
        Z,X=heapq.heappop(q)
        if Z<=a:
            continue
        if not visited[X]:
            visited[X]=True
            result+=Z
            cnt+=1
            for i in tmp[X]:
                if not visited[i[1]]:
                    heapq.heappush(q,i)
    if cnt==N-1:
        return result
    else:
        return 0

N,M,T=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append((i+1,b))
    graph[b].append((i+1,a))

answer=[]
for i in range(T):
    result=MST(i,graph)
    if result==0:
        break
    answer.append(result)

while len(answer)<T:
    answer.append(0)

print(*answer)