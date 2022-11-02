import sys
input=sys.stdin.readline


N,W=map(int,input().split())
Nodes=[[] for i in range(N+1)]
visited=[False for j in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    Nodes[a].append(b)
    Nodes[b].append(a)
    
def cntLeafNodes (node):
    global cnt
    visited[node]=True;
    if (len(Nodes[node])==1 & visited[Nodes[node][0]]):
        cnt+=1
        return
    for nextNode in Nodes[node]:
        if not visited[nextNode]:
            cntLeafNodes(nextNode)

cnt=0        
cntLeafNodes(1)
print(W/cnt)
    