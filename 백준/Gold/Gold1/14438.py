import sys
input=sys.stdin.readline

def init(start,end,index):
    if start==end:
        tree[index]=arr[start]
    else:
        mid=(start+end)//2
        init(start,mid,index*2)
        init(mid+1,end,index*2+1)
        tree[index]=min(tree[index*2],tree[index*2+1])
    return tree[index]

def update(start,end,index,what,value):
    if start>what or end<what:
        return
    if start==end:
        tree[index]=value
        return
    mid=(start+end)//2
    update(start,mid,index*2,what,value)
    update(mid+1,end,index*2+1,what,value)
    tree[index]=min(tree[index*2],tree[index*2+1])
    
def find_min(start,end,index,left,right):
    if left>end or right<start:
        return sys.maxsize
    if left<=start and right>=end:
        return tree[index]
    mid=(start+end)//2
    return min(find_min(start,mid,index*2,left,right),find_min(mid+1,end,index*2+1,left,right))

N=int(input())
arr=list(map(int,input().rstrip().split()))

tree=[0]*(N*4)
init(0,N-1,1)

for _ in range(int(input())):
    a,b,c,=map(int,input().split())
    if a==1:
        update(0,N-1,1,b-1,c)
        arr[b-1]=c
    elif a==2:
        print(find_min(0,N-1,1,b-1,c-1))