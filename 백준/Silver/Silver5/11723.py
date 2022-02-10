import sys
input=sys.stdin.readline

S=set()

for _ in range(int(input())):
    order=input().strip().split()
    if len(order)==1:
        if order[0]=='all':
            S=set([i for i in range(1,21)])
        else:
            S=set()
        continue
    
    order, value = order[0], order[1]
    value=int(value)

    if order=='add':
        S.add(value)
    elif order=='remove':
        if value in S:
            S.discard(value)
    elif order=='check':
        print(1 if value in S else 0)
    elif order=='toggle':
        if value in S:
            S.discard(value)
        else:
            S.add(value)


