nA,nB=map(int,input().split())

A,B={},{}
for n in map(int,input().split()):
    A[n]=True
for n in map(int,input().split()):
    if n in A:
        del(A[n])
print(A)