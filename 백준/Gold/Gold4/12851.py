from collections import deque

def bfs(l,k):
    c=0
    store=[]
    dq=deque()
    for i in l:
        dq.append(i)
    while dq:
        pos=dq.popleft()
        for i in (pos-1,pos+1,pos*2):
            if 0<=i<100001:
                if visited[i][0]==0:
                    store.append(i)
                    visited[i][0]=1
                    visited[i][1]=k
                elif visited[i][0]!=0 and visited[i][1]==k:
                    store.append(i)
                if i==K:
                    c+=1
    return store,c

N,K=map(int,input().split())
if N==K:
    print(0)
    print(1)
else:
    cnt=0
    result=[N]
    visited=[[0,0] for _ in range(100001)]
    while True:
        result,check=bfs(result,cnt)
        cnt+=1
        if check!=0:
            print(cnt)
            print(check)
            break
