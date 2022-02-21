import sys
input=sys.stdin.readline


N=int(input())
print(*sorted(list(map(int,input().split()))))