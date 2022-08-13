from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0 for _ in range(N+1)]
for i in range(1,N+1):
    if visited[i]==0:
        dq=deque()
        dq.append(i)
        visited[i]=1
        while dq:
            X=dq.popleft()
            for j in graph[X]:
                if visited[j]==0:
                    visited[j]=visited[X]*(-1)
                    dq.append(j)
                elif visited[j]==visited[X]:
                    print(0)
                    exit(0)

print(1)
            