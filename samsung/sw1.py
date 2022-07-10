import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    samsung=[]
    for _ in range(N):
        samsung.append(list(map(int,input().split())))