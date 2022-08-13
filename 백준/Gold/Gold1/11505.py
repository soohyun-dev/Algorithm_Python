import sys
input=sys.stdin.readline

tmp=1000000007

def init(start,end,index):
    if start==end:
        tree[index]=arr[start]
    else:
        mid=(start+end)//2
        tree[index]=init(start,mid,index*2)*init(mid+1,end,index*2+1)%tmp
    return tree[index]

def update(start,end,index,what,value):
    if what < start or what > end:
        return
    if start==end:
        tree[index]=value
        return
    mid=(start+end)//2
    update(start,mid,index*2,what,value)
    update(mid+1,end,index*2+1,what,value)
    tree[index]=tree[index*2]*tree[index*2+1]%tmp
    
def interval_multi(start,end,index,left,right):
    if end<left or start>right:
        return 1
    if left<=start and right>=end:
        return tree[index]
    mid=(start+end)//2
    return interval_multi(start,mid,index*2,left,right)*interval_multi(mid+1,end,index*2+1,left,right)%tmp
    

N,M,K=map(int,input().split())
arr=[int(input().rstrip()) for _ in range(N)]
tree=[0]*(N*4)

init(0,N-1,1)

for j in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        update(0,N-1,1,b-1,c)
        arr[b-1]=c
    elif a==2:
        print(interval_multi(0,N-1,1,b-1,c-1))
        
        
        