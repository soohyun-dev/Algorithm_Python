from collections import deque
import sys
input=sys.stdin.readline

def bfs(i):
    dq=deque()
    dq.append(i)
    color[i]=1
    while dq:
        X=dq.popleft()
        for k in graph[X]:
            if color[k]==0:
                dq.append(k)
                color[k]=color[X]*(-1)
            elif color[X]==color[k]:
                return False
    

for _ in range(int(input())):
    V,E=map(int,input().rstrip().split())
    graph=[[] for _ in range(V+1)]
    for i in range(E):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    color=[0 for _ in range(V+1)]
    check=True
    for i in range(1,V+1):
        if color[i]==0:
            result=bfs(i) 
            if result==False:
                check=False
                print('NO')
                break
    if check==True:     
        print('YES')
                
                    
        
            