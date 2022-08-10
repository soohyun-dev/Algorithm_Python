from collections import deque
import sys
input=sys.stdin.readline

def dfs(x):
    dq=deque()
    dq.append(x)
    store=[]
    while dq:
        X=dq.popleft()
        tmp=nums[X-1][1]
        if visited[tmp]==0:
            dq.append(tmp)
            visited[tmp]=1
            store.append(tmp)
        elif X==x:
            return store
        elif tmp==X:
            return [X]
    for i in store:
        visited[i]=0
    return []

N=int(input())
nums=[[i,int(input())] for i in range(1,N+1)]
visited=[0 for _ in range(N+1)]
result=[]
for j in range(1,N+1):
    if visited[j]==0:
        tmp=dfs(j)
        for k in tmp:
            result.append(k)
result.sort()
print(len(result))
for i in result:
    print(i)