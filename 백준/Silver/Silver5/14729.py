import sys
input=sys.stdin.readline

N=int(input())
score=[]
for i in range(N):
    score.append(float(input()))
score.sort()
for i in range(7):
    print("{:.3f}".format(score[i]))


    