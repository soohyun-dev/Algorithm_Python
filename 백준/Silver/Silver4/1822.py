import sys
input=sys.stdin.readline

nA,nB=map(int,input().split())
A,B={},{}
for n in map(int,input().split()):
    A[n]=True
for n in map(int,input().split()):
    if n in A:
        del(A[n])

if len(A)==0:
    print(0)
else:
    print(len(A))
    print(*sorted(A))