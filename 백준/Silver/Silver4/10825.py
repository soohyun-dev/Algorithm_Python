import sys

input = sys.stdin.readline

N=int(input())
score=[]
for i in range(N):
    score.append(list(map(str,input().split())))
score.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(score[i][0])


    