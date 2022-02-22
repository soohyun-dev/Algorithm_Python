import sys
input=sys.stdin.readline

N=int(input())
score=[]
for i in range(N):
    score.append(float(input()))
score.sort(reverse=True)
l=score[-7:]
print(l)