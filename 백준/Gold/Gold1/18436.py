import sys
input=sys.stdin.readline

def init(start,end,index):
    if start==end:
        if arr[start]%2==0:
            tree[index][0]=1
        else:
            tree[index][1]=1
    else:
        mid=(start+end)//2
        init(start,mid,index*2)
        init(mid+1,end,index*2+1)
        tree[index]=[tree[index*2][0]+tree[index*2+1][0],tree[index*2][1]+tree[index*2+1][1]]
    return tree[index]

def update(start,end,index,w,v):
    if w<start or w>end:
        return
    if start==end:
        if v%2==0:
            tree[index]=[1,0]
        else:
            tree[index]=[0,1]
        return tree[index]
    mid=(start+end)//2
    update(start,mid,index*2,w,v)
    update(mid+1,end,index*2+1,w,v)
    tree[index]=[tree[index*2][0]+tree[index*2+1][0],tree[index*2][1]+tree[index*2+1][1]]

def find_result(start,end,index,left,right):
    if start>right or end <left:
        return [0,0]
    if left<=start and right>=end:
        return tree[index]
    mid=(start+end)//2
    left_node=find_result(start,mid,index*2,left,right)
    right_node=find_result(mid+1,end,index*2+1,left,right)
    return [left_node[0]+right_node[0],left_node[1]+right_node[1]]

N=int(input())
arr=list(map(int,input().rstrip().split()))
tree=[[0,0] for _ in range(N*4)]

init(0,N-1,1)
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a==1:
        if arr[b-1]%2==c%2:
            arr[b-1]=c
            continue
        else:
            update(0,N-1,1,b-1,c)
            arr[b-1]=c
        
    elif a==2:
        print(find_result(0,N-1,1,b-1,c-1)[0])
    elif a==3:
        print(find_result(0,N-1,1,b-1,c-1)[1])
