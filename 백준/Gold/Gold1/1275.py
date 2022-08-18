import sys
input=sys.stdin.readline

def init(start,end,index):
    if start==end:
        tree[index]=arr[start]
    else:
        mid=(start+end)//2
        tree[index]=init(start,mid,index*2)+init(mid+1,end,index*2+1)
    return tree[index]
    
def update(start,end,index,w,v):
    tree[index]+=v
    if start==end:
        return 
    mid=(start+end)//2
    if start<=w<=mid:
        update(start,mid,index*2,w,v,)
    else:
        update(mid+1,end,index*2+1,w,v)

def range_sum(start,end,index,left,right):
    if left>end or start>right:
        return 0
    if left <=start and end<= right:
        return tree[index]
    mid=(start+end)//2
    return range_sum(start,mid,index*2,left,right)+range_sum(mid+1,end,index*2+1,left,right)

N,Q=map(int,input().split())
arr=list(map(int,input().split()))
tree=[0]*(N*4)
init(0,N-1,1)
for i in range(Q):
    a,b,c,d=map(int,input().split())
    print(range_sum(0,N-1,1,a-1,b-1))
    tmp=d-arr[c-1]
    arr[c-1]=d
    update(0,N-1,1,c-1,tmp)