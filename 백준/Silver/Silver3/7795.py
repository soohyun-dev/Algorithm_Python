import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    A=sorted(list(map(int,input().split())), reverse=True)
    B=sorted(list(map(int,input().split())), reverse=True)
    a=0
    b=0
    total=0
    
    while a<N and b<M:
        if A[a] > B[b]:
            total+=M-b
            a+=1
        else:
            b+=1
            
    print(total)


