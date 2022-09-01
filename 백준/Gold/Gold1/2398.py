from cmath import inf
import heapq
import sys
input=sys.stdin.readline

def dijkstra(start):
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

DA=dijkstra(A)
DB=dijkstra(B)
DC=dijkstra(C)
cnt=0
leng=inf
point=0
for i in range(1,N+1):
    if DA[0][i]+DB[0][i]+DC[0][i]<leng:
        point=i
        leng=DA[0][i]+DB[0][i]+DC[0][i] 
         
new_arr=list()
new_arr+=(returnRoad(A,point,DA[1]))        
new_arr+=(returnRoad(B,point,DB[1]))   
new_arr+=(returnRoad(C,point,DC[1]))  

print(leng,len(new_arr))
for i,j in new_arr:
    print(i,j)