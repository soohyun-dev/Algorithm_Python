from cmath import inf
import heapq
import sys
input=sys.stdin.readline

for k in range(int(input())):
    M,N=map(int,input().split())
    graph=[[] for _ in range(N)]
    for i in range(M):
        a,b,c=map(int,input().split())
        graph[a].append((c,b,a))
        graph[b].append((c,a,b))
        
    dist=[inf]*N
    dist[0]=0
    arr=[0]*N
    q=[(0,0,0)]
    while q:
        Z,X,Y=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next,now in graph[X]:
            cost+=Z
            if cost < dist[next]:
                dist[next]=cost
                arr[next]=now
                heapq.heappush(q,[cost,next,now])
    check=[N-1]
    if dist[N-1]==inf:
        print('Case #%d: %d' %(k+1, -1))
    else:
        end=N-1
        while 0!=end:
            check.append(arr[end])
            end=arr[end]
        check.reverse()
        print("Case #%d: " %(k+1), end='')
        print(*check)