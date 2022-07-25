from collections import deque

def bfs(graph,start):
    dq=deque()
    dq.append(graph[start])
    check=[[0,0] for _ in range(N+1)]
    check[start][0],check[start][1]=1,1
    cnt=2
    while dq:
        n=dq.popleft()
        n.sort(reverse=True)
        for i in n:
            if check[i][1]==0:     
                check[i][0]=cnt
                check[i][1]=1
                cnt+=1
                dq.append(graph[i])
    for i in range(1,N+1):
        print(check[i][0])

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
bfs(graph,R)