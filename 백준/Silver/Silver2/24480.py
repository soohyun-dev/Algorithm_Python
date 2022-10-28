import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(start):
    global cnt
    for i in graph[start]:
        if not visited[i]:
            visited[i]=True
            check[i]=cnt
            cnt+=1
            DFS(i) 

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
check=[0]*(N+1)
check[R]=1
visited=[False]*(N+1)
visited[R]=True
cnt=2
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for j in range(1,N+1):
    graph[j].sort(reverse=True)
    
DFS(R)

for k in range(1, N+1):
    print(check[k])