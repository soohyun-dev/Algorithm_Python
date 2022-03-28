import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    A=sorted(list(map(int,input().split())), reverse=True)
    B=sorted(list(map(int,input().split())), reverse=True)
    cnt_A=0
    cnt_B=0
    total=0

    while cnt_A<N and cnt_B<M:
        if A[cnt_A] > B[cnt_B]:
            total+=M-cnt_B
            cnt_A+=1
        else:
            cnt_A+=1            
            
    print(total)

