import sys
input=sys.stdin.readline
from collections import deque

K,L=map(int, input().split())
store=dict()
for i in range(L):
    ID=input().rstrip()
    store[ID]=i

chart=sorted(store.items(), key=lambda item:item[1])
cnt=0
for id in chart:
    print(id[0])
    cnt+=1
    if cnt==K:
        break