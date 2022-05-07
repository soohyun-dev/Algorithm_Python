import sys
input=sys.stdin.readline

N=int(input())
for i in range(N):
    if i==0:
        order=list(input())
    else:
        tmp=list(input())

    if i>0:
        for j in range(len(order)):
            if order[j]!=tmp[j]:
                order[j]='?'
print(*order, sep='')
