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
    if w<start or w>end:
        return
    tree[index]+=v
    if start==end:
        return 
    mid=(start+end)//2
    update(start,mid,index*2,w,v)
    update(mid+1,end,index*2+1,w,v)
    
def range_sum(start,end,index,left,right):
    if left>end or right<start:
        return 0
    if start>=left and right>=end:
        return tree[index]
    mid=(start+end)//2
    return range_sum(start,mid,index*2,left,right)+range_sum(mid+1,end,index*2+1,left,right)

N,M=map(int,input().split())
arr=[ 0 for _ in range(N)]
tree=[0]*(N*4)

init(0,N-1,1)

for i in range(M):
    a,b,c=map(int,input().split())
    if a==0:
        print(range_sum(0,N-1,1,b-1,c-1))
    elif a==1:
        tmp=c-arr[b-1]
        arr[b-1]=c
        update(0,N-1,1,b-1,tmp)