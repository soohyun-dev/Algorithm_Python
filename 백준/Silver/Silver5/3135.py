import sys
input=sys.stdin.readline

A,B=map(int,input().split())
N=int(input())
m=1000
for i in range(N):
    num=int(input())
    if m > abs(B-num):
        change=num
        m=abs(B-num)
sum=1
if abs(A-B) <= abs(change-B):
    print(abs(A-B))
else:
    sum+=abs(change-B)
    print(sum)


