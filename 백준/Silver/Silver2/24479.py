import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

cnt=1
def DFS(start):
    global cnt
    for i in graph[start]:
        if not visited[i]:
            cnt+=1
            visited[i]=True
            cntChk[i]=cnt
            DFS(i)

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
cntChk=[0]*(N+1)
visited=[False]*(N+1)
cntChk[R]=1
visited[R]=True

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1,N+1):
    graph[j].sort()

DFS(R)

for k in range(1,N+1):
    print(cntChk[k])