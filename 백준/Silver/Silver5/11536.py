import sys
input=sys.stdin.readline
names=[]
N=int(input())
for i in range(N):
    names.append(input().rstrip())

if sorted(names)==names:
    print('INCREASING')
elif sorted(names, reverse=True)==names:
    print('DECREASING')
else:
    print('NEITHER')
