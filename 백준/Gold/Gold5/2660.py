from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
l=[[] for _ in range(N+1)]
while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    l[a].append(b)
    l[b].append(a)


def bfs(x):
    dq=deque()
    dq.append(x)
    cnt=[0 for _ in range(N+1)]
    cnt[x]=1
    while dq:
        a=dq.popleft()
        for i in l[a]:
            if cnt[i]==0:
                cnt[i]=cnt[a]+1
                dq.append(i)
    del(cnt[x])
    return max(cnt)
        
result=[]
for i in range(1,N+1):
    result.append(bfs(i))

MIN=min(result)
answer=[]
for i in range(N):
    if result[i]==MIN:
        answer.append(i+1)
print(MIN-1, len(answer))
print(*answer)