from collections import deque

def bfs():
    while dq:
        pos=dq.popleft()
        if pos==K:
            print(check[K])
            break
        
        for i in (pos*2,pos-1,pos+1):
            if i==pos*2:
                if 0<=i<=100000 and check[i]==0:
                    check[i]=check[pos]
                    dq.append(i)
            else:
                if 0<=i<=100000 and check[i]==0:
                    check[i]=check[pos]+1
                    dq.append(i)

N,K=map(int,input().split())
check=[0]*100001
dq=deque()
dq.append(N)
bfs()