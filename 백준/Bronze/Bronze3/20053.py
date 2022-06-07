import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N=int(input())

    l=sorted(list(map(int,input().split())))
    print(l[0], l[-1])
    
    