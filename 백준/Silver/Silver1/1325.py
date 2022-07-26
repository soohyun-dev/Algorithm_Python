from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
LIST=[]
graph=[[] for _ in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    LIST.append(y)
    graph[y].append(x)

def bfs(start):
    tmp=0
    dq=deque()
    dq.append([start,0])
    visited=[False]*(N+1)
    visited[start]=True
    while dq:
        node,cnt=dq.popleft()
        for i in graph[node]:
            if visited[i]==False:
                visited[i]=True
                dq.append([i,cnt+1])
                tmp+=1
    return tmp

MAX=0
answer=[]
LIST=set(LIST)
for i in LIST:
    if graph[i]:
        result=bfs(i)
        if MAX < result:
            MAX=result
            answer=[i]
        elif MAX==result:
            answer.append(i)

print(*answer)
        
    

