def init(start,end,index):
    if start==end:
        tree[index]=arr[start]
    else:
        mid=(start+end)//2
        tree[index]=max(init(start,mid,index*2),init(mid+1,end,index*2+1))
    return tree[index]

def getMax(start,end,index,left,right):
    if start>right or end<left:
        return 0
    if start>=left and right>=end:
        return tree[index]
    mid=(start+end)//2
    return max(getMax(start,mid,index*2,left,right), getMax(mid+1,end,index*2+1,left,right))
    
N,M=map(int,input().split())
arr=list(map(int,input().split()))
tree=[0]*(N*4)

init(0,N-1,1)

for i in range(M-1,N-M+1):
    print(getMax(0,N-1,1,i-M+1,i+M-1),end=' ')