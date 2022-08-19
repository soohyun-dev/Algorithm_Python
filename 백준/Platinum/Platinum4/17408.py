import sys
input=sys.stdin.readline

def init(start,end,index):
    if start==end:
        tree[index]=[arr[start],start]
    else:
        mid=(start+end)//2
        left_node=init(start,mid,index*2)
        right_node=init(mid+1,end,index*2+1)
        if left_node[0]>right_node[0]:
            tree[index]=left_node
        else:
            tree[index]=right_node
    return tree[index]

def update(start,end,index,w,v):
    if w<start or w>end:
        return tree[index]
    if start==end:
        tree[index]=[v,w]
        return tree[index]
    mid=(start+end)//2
    left_node=update(start,mid,index*2,w,v)
    right_node=update(mid+1,end,index*2+1,w,v)
    if left_node[0]>right_node[0]:
        tree[index]=left_node
    else:
        tree[index]=right_node
    return tree[index]
    
def getMax(start,end,index,left,right):
    if start>right or end < left:
        return [0,0]
    if start>=left and right>=end:
        return tree[index]
    mid=(start+end)//2
    left_node=getMax(start,mid,index*2,left,right)
    right_node=getMax(mid+1,end,index*2+1,left,right)
    if left_node[0]>right_node[0]:
        return left_node
    else:
        return right_node


N=int(input())
arr=list(map(int,input().rstrip().split()))
arr=[0]+arr
tree=[[0,0] for _ in range(N*4)]

init(1,N,1)

M=int(input())
for i in range(M):
    a,b,c=map(int,input().split())
    if a==1:
        arr[b]=c
        update(1,N,1,b,c)
    elif a==2:
        result=getMax(1,N,1,b,c)
        left_MAX=getMax(1,N,1,b,result[1]-1)
        right_MAX=getMax(1,N,1,result[1]+1,c)
        print(result[0]+max(left_MAX[0],right_MAX[0]))
        
        
        
