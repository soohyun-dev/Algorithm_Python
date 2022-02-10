import sys
input=sys.stdin.readline

N=int(input())
T=[sorted(list(map(int,input().split()))) for _ in range(N)]

for i in range(N):
    print(T[i][-3])

    