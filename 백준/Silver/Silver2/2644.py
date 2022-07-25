from collections import deque
import sys
input=sys.stdin.readline

def bfs(graph,X,Y):
    course=[0]*(N+1)
    dq=deque()
    dq.append(X)
    check=[X]
    while dq:
        X=dq.popleft()
        for j in graph[X]:
            if j not in check:
                course[j]=course[X]+1
                check.append(j)
                dq.append(j)
    result=course[Y]
    if result==0:
        return -1
    else:
        return result

N=int(input())
a,b=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(int(input())):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(graph,a,b))