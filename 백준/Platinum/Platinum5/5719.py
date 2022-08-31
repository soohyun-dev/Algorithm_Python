from cmath import inf
import heapq
import sys
input=sys.stdin.readline

def dijkstra(start,end):
    dist=[inf]*(N)
    befNode=[0]*(N)
    q=[(0,start,0)]
    while q:
        Z,X,Y=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next,now in graph[X]:
            cost+=Z
            if cost<dist[next]:
                dist[next]=cost
                befNode[next]=now
                heapq.heappush(q,[cost,next,now])        

    return (befNode,dist[end])

def delnode(result,start,end):
    arr=result[0]
    tmp=end
    check=[]
    while start!=tmp:
        check.append([arr[tmp],tmp])
        tmp=arr[tmp]
        
    for a,b in check:
        for i in graph[a]:
            if i[1]==b:
                graph[a].remove(i)
                break

while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    start,end=map(int,input().split())
    graph=[[] for _ in range(N)]
    for i in range(M):
        a,b,c=map(int,input().split())
        graph[a].append((c,b,a))

    result=dijkstra(start,end)
    MIN=result[1]
    delnode(result,start,end)
    result2=dijkstra(start,end)
    
    while result2[1]==MIN:
        delnode(result2,start,end)
        result2=dijkstra(start,end)
    
    if result2[1]==inf:
        print(-1)
    else:
        print(result2[1])