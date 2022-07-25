from collections import deque

def bfs():
    while dq:
        pos=dq.popleft()
        if pos==K:
            print(check[K]-1)
            break
        
        for i in (pos-1,pos+1,pos*2):
            if 0<=i<=100000 and check[i]==0:
                if i==pos*2:
                    check[i]=check[pos]
                    dq.appendleft(i)
                else:
                    check[i]=check[pos]+1
                    dq.append(i)

N,K=map(int,input().split())
check=[0]*100001
check[N]=1
dq=deque()
dq.append(N)
bfs()