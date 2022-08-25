import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
start,end=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
check=[0]*(N+1)
check[start]=sys.maxsize
q=[]
heapq.heappush(q,(-sys.maxsize, start))

while q:
    Z,X=heapq.heappop(q)
    print(X)
    Z=-Z
    if check[X]<=Z:
        for x,y in graph[X]:
            MIN=min(x,Z)
            if check[y]<MIN:
                check[y]=MIN
                heapq.heappush(q,(-MIN,y))

print(check[end])