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

def dayChange(start,end,index,left,right):
    if left>end or right<start:
        return 0
    if left<=start and right>=end:
        return tree[index]
    mid=(start+end)//2
    return dayChange(start,mid,index*2,left,right)+dayChange(mid+1,end,index*2+1,left,right)

N,Q=map(int,input().split())
arr=[0]*N
tree=[0]*(N*4)

for i in range(Q):
    a,b,c=map(int,input().split())
    if a==1:
        arr[b-1]=c
        update(0,N-1,1,b-1,c)
    elif a==2:
        print(dayChange(0,N-1,1,b-1,c-1))
        
