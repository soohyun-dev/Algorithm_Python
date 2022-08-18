import sys
input=sys.stdin.readline

def init(start,end,index):
    if start==end:
        if arr[start]>0:
            tree[index]=1
        elif arr[start]<0:
            tree[index]=-1
        else:
            tree[index]=0
    else:
        mid=(start+end)//2
        tree[index]=init(start,mid,index*2)*init(mid+1,end,index*2+1)
    return tree[index]

def update(start,end,index,w,v):
    if w<start or w>end:
        return
    if start==end:
        tree[index]=v
        return tree[index]
    mid=(start+end)//2
    update(start,mid,index*2,w,v)
    update(mid+1,end,index*2+1,w,v)
    tree[index]=tree[index*2]*tree[index*2+1]
    
def rangeGop(start,end,index,left,right):
    if left>end or start>right:
        return 1
    if start>=left and right>=end:
        return tree[index]
    mid=(start+end)//2
    return rangeGop(start,mid,index*2,left,right)*rangeGop(mid+1,end,index*2+1,left,right) 
    
while True:
    try:
        N,M=map(int,input().split())
        arr=list(map(int,input().split()))
        tree=[0]*(N*4)
        
        init(0,N-1,1)
        
        for i in range(M):
            a,b,c,=input().split()
            b,c=int(b),int(c)
            if a=='C':
                arr[b-1]=c
                if c<0:
                    update(0,N-1,1,b-1,-1)
                elif c>0:
                    update(0,N-1,1,b-1,1)
                else:
                    update(0,N-1,1,b-1,0)
            elif a=='P':
                answer=rangeGop(0,N-1,1,b-1,c-1)
                if answer>0:
                    print('+',end='')
                elif answer<0:
                    print('-',end='')
                else:
                    print(0,end='')
        print()
    except:
        break