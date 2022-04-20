import sys
from tokenize import Double
input=sys.stdin.readline

while True:
    N=int(input())
    if N==0:
        break
    names=[]
    mh=0
    for i in range(N):
        names.append(input().split())
        mh=max(mh,float(names[i][1]))
    for i in range(N):
        if float(names[i][1])==mh:
            print(names[i][0], end=" ")
    print()