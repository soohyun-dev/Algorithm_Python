import sys
input=sys.stdin.readline

def init(start,end,index):  # 세그먼트 트리 생성 함수
    if start==end:
        tree[index]=arr[start]
        return tree[index]
    mid=(start+end)//2
    tree[index]=init(start,mid,index*2)+init(mid+1,end,index*2+1)
    return tree[index]

def interval_sum(start,end,index,left,right):  # 구간 합 구하는 함수
    if left>end or right<start:
        return 0
    if left<=start and right >= end:
        return tree[index]
    mid=(start+end)//2
    return interval_sum(start,mid,index*2,left,right)+interval_sum(mid+1,end,index*2+1,left,right)

def update(start,end,index,what,value):
    if what < start or what > end:
        return
    tree[index]+=value
    if start==end:
        return 
    mid=(start+end)//2
    update(start,mid,index*2,what,value)
    update(mid+1,end,index*2+1,what,value)
    
N,M,K=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
tree=[0]*(len(arr)*4)

init(0,len(arr)-1,1)  # 트리 생성

for j in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        ch=c-arr[b-1]
        arr[b-1]=c
        update(0,len(arr)-1,1,b-1,ch)  
    elif a==2:
        print(interval_sum(0,len(arr)-1,1,b-1,c-1))
