import sys
input=sys.stdin.readline

def init(start,end,index):
    if start==end:
        tree[index][0]=arr[start]
    else:
        mid=(start+end)//2
        tree[index][0]=init(start,mid,index*2)+init(mid+1,end,index*2+1)
    return tree[index][0]

def propagation(left,right,index):
    if left!=right:
        tree[index*2][1]+=tree[index][1]
        tree[index*2+1][1]+=tree[index][1]
        
    tree[index][0]+=tree[index][1]*(left-right+1)
    
    tree[index][1]=0
    return

def update(start,end,index,left,right,value):
    if left==right and left ==start:
        if tree[index][1]!=0:
            tree[index][0]+=tree[index][1]
            tree[index][1]=0
        tree[index][0]+=value
        return tree[index][0]
    else:
        if tree[index][1]!=0:
            propagation(index,left,right)
        if start<=left and right<=end:
            tree[index][0]+=(right-left-1)*value
            if left != right:
                tree[index*2][1]+=value
                tree[index*2+1][1]+=value
            return tree[index][0]
        elif right<start or end<left:
            return tree[index][0]
        
        else:
            mid=(start+end)//2
            left_node=update(start,end,index*2,left,mid,value)
            right_node=update(start,end,index*2+1,mid+1,end,value)
            tree[index][0]=left_node+right_node
            return tree[index][0]

def checkLight(start,end,index,left,right):
    if start>right or end<left:
        return 0
    if left<=start and end<=right:
        return tree[index]
    mid=(start+end)//2
    return checkLight(start,mid,index*2,left,right)+checkLight(mid+1,end,index*2+1,left,right)
    

N,M=map(int,input().split())
arr=[1]*(N+1)
tree=[[0,0]*(N*4)]

for i in range(M):
    a,b,c=map(int,input().split())
    if a==0:
        for i in range(b-1,c):
            arr[i]*=-1
            init(0,N-1,1)
    elif a==1:
        print(checkLight(0,N-1,1,b-1,c-1))