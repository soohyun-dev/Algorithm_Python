from collections import deque

def bfs(l,k):
    store=[]
    dq=deque()
    c=0
    for i in (l):
        dq.append(i)
    while dq:
        X=dq.popleft()
        for i in (X-1,X+1,X*2):
            if 0<=i<100001:
                if visited[i][0]==0:
                    store.append(i)
                    visited[i][0]=k
                    visited[i][1]=X
        if X==K:
            tmp=K
            answer=[]
            for _ in range(visited[tmp][0]+1):
                answer.append(tmp)
                tmp=visited[tmp][1]
            print(k-1)
            print(*answer[::-1])
            c+=1
    return store,c

N,K=map(int,input().split())
if N==K:
    print(0)
    print(N)
else:
    visited=[[0,0] for _ in range(100001)]
    cnt=1
    result=[N]
    while True:
        result,check=bfs(result,cnt)
        cnt+=1
        if check!=0:
            break
