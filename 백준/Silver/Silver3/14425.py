import sys
input=sys.stdin.readline

N,M=map(int,input().split())
S={}
for _ in range(N):
    S[input()]=True

cnt=0
for _ in range(M):
    if S.get(input()) ==True:
        cnt+=1
    
print(cnt)

