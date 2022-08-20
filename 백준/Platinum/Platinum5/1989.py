def init(MAX,start,end,index):
    if start==end:
        tree[index]=[arr[start],arr[start],arr[start]*arr[start]]
    else:
        mid=(start+end)//2
        left_node=init(MAX,start,mid,index*2)
        right_node=init(MAX,mid+1,end,index*2+1)
        tree[index][0]=left_node[0]+right_node[0]
        tree[index][1]=min(left_node[1],right_node[1])
        tree[index][2]=tree[index][0]*tree[index][1]
        if MAX<tree[index][2]:
            MAX=tree[index][2]
        print(MAX)
    return tree[index]

# def getMax(start,end,index,left,right):
#     if start>right or end<left:
#         return [0,0,0]
#     if start<=left and right>=end:
#         return tree[index]
#     mid=(start+end)//2
#     left_node=getMax(start,mid,index*2,left,right)
#     right_node=getMax(mid+1,end,index*2+1,left,right)
    

N=int(input())
arr=list(map(int,input().split()))
arr=[0]+arr
MAX=0
tree=[[0,0,0] for _ in range(N*4)]
init(MAX,1,N,1)
print(MAX)