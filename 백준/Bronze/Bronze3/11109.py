import sys
input=sys.stdin.readline

for _ in range(int(input())):
    d,n,s,p=map(int,input().split())
    A=n*s
    B=d+n*p
    if A<B:
        print('do not parallelize')
    elif A>B:
        print('parallelize')
    else:
        print('does not matter')
        