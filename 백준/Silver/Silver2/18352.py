from collections import deque

N,M,K,X=map(int,input().split())
cities=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    cities[a].append(b)

def bfs(start):
    dq=deque()
    dq.append([start,0])
    answer=[]
    visited=[False for _ in range(N+1)]
    visited[start]=True
    while dq:
        x,y=dq.popleft()
        for i in cities[x]:
            if visited[i]==False:
                dq.append([i,y+1])
                visited[i]=True
                if y+1==K:
                    answer.append(i)
                    dq.pop()
    return answer
        
result=bfs(X)

if len(result)==0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)