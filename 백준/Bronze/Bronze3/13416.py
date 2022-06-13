import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    result=0
    for i in range(N):
        A,B,C=map(int,input().split())
        stock=max(A,B,C)
        if stock>0:
            result+=stock
    print(result)