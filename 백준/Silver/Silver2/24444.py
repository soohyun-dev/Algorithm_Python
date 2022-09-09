from collections import deque
import sys
input =sys.stdin.readline

def BFS(start):
    cnt=2
    visited[start]=True
    check[start]=1
    q=deque()
    q.append(start)
    while q:
        X=q.popleft()
        for i in graph[X]:
            if not visited[i]:
                visited[i]=True
                check[i]=cnt
                cnt+=1
                q.append(i)
    return

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
check=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for j in graph:
    j.sort()

BFS(R)
for i in range(1,N+1):
    print(check[i])