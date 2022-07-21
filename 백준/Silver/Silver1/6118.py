import sys
input=sys.stdin.readline
from collections import deque

def bfs(num):
    MAX=-1
    dq=deque()
    dq.append(num)
    nums=[0]*(N+1)
    nums[1]=1
    while dq:
        n=dq.popleft()
        for j in graph[n]:
            if nums[j]==0:
                nums[j]=nums[n]+1
                dq.append(j)
                if MAX<nums[j]:
                    MAX=nums[j]
                    ind=j
                    cnt=1
                elif MAX==nums[j]:
                    if ind>j:
                        ind=j
                    cnt+=1
    return ([ind, MAX-1, cnt])

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(*bfs(1))