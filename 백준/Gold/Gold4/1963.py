from collections import deque

prime=[True]*10001
prime[0],prime[1]=False,False

for i in range(2,101):
    if prime[i]==True:
        for j in range(i+i,10001,i):
            prime[j]=False
    
def bfs(x,y):
    dq=deque()
    dq.append([x,0])
    visitied=[False]*10001
    visitied[x]=True
    while dq:
        num,cnt=dq.popleft()
        tmp=str(num)
        for i in range(4):
            for j in range(10):
                if i==0 and j==0:
                    j+=1
                NUM=int(tmp[:i] + str(j) + tmp[i+1:])
                if prime[NUM]==True and visitied[NUM]==False:
                    dq.append([NUM,cnt+1])
                    visitied[int(NUM)]=True
                    if NUM==y:
                        return cnt+1
                    
for i in range(int(input())):
    start,end=map(int,input().split())
    if start==end:
        print(0)
    else:
        result=bfs(start,end)
        if result==None:
            print('Impossible')
        else:
            print(result)