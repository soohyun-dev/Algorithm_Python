from cmath import inf
import heapq
import sys
input=sys.stdin.readline

def dijkstra(start,end):
    q=[(0,start,0)]
    dist=[inf]*(N+1)
    dist[start]=0
    arr=[0]*(N+1)
    while q:
        Z,X,Y=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next,now in graph[X]:
            cost+=Z
            if cost<dist[next]:
                dist[next]=cost
                arr[next]=now
                heapq.heappush(q,[cost,next,now])
    return [dist,arr]

def returnRoad(start,end,arr):
    tmp=[]
    while start!=end:
        tmp.append([arr[end],end])
        end=arr[end]
    return tmp

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b,a))
    graph[b].append((c,a,b))
A,B,C=map(int,input().split())

result=[]

AB=dijkstra(A,B)
result+=returnRoad(A,B,AB[1])
AC=dijkstra(A,C)
result+=returnRoad(A,C,AC[1])
BC=dijkstra(B,C)
result+=returnRoad(B,C,BC[1])

new_arr=[]
for i in result:
    A=i
    B=[A[1],A[0]]
    if A not in new_arr and B not in new_arr :
        new_arr.append(i)

cnt=0
for j in new_arr:
    for k in graph[j[0]]:
        if k[1]==j[1]:
            cnt+=k[0]
            break
    for n in graph[j[1]]:
        if k[1]==j[0]:
            cnt+=k[0]
            break
print(cnt, len(new_arr))
for i in new_arr:
    print(*i)