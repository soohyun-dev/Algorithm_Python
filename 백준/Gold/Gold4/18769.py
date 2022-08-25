import heapq
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N,M=map(int,input().split())
    graph=[[[] for _ in range(M+1)] for _ in range(N+1)]
        
    for i in range(1,N+1):
        lr=[0]+list(map(int,input().split()))
        for j in range(1,M):
            graph[i][j+1].append((lr[j],i,j))
            graph[i][j].append((lr[j],i,j+1))
    for i in range(1,N):
        ud=[0]+list(map(int,input().split()))
        for j in range(1,M+1):
            graph[i][j].append((ud[j],i+1,j))
            graph[i+1][j].append((ud[j],i,j))
    visited=[[False for _ in range(M+1)] for _ in range(N+1)]
    visited[1][1]=True            
    q=graph[1][1]
    heapq.heapify(q)
    result=0
    cnt=0
    while q:
        Z,X,Y=heapq.heappop(q)
        if not visited[X][Y]:
            visited[X][Y]=True
            result+=Z
            cnt+=1
            if cnt==N*M-1:
                break
            for i in graph[X][Y]:
                if not visited[i[1]][i[2]]:
                    heapq.heappush(q,i)
    print(result)