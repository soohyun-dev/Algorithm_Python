import sys
input=sys.stdin.readline

N=int(input())
num=list(map(int, input().split()))
K=[num[0]]
for i in range(1,N):
    K.append(K[-1]+num[i])

M=int(input())
for i in range(M):
    start,end=map(int,input().split())
    print(K[end-1]-K[start-1])