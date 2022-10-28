import sys
input=sys.stdin.readline

N=int(input())
tree=[0]*(N+1)
for i in range(N-1):
    a,b=map(int,input().split(' '))
    tree[a]+=1
    tree[b]+=1
    
T=int(input())
for j in range(T):
    q,k=map(int,input().split(' '))
    if q==1:
        if tree[k]==1: print('no')
        else: print('yes')
    else: print('yes')        