import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    ranking=[]
    sum=0
    for i in range(1,N+1):
        vote=int(input())
        ranking.append([i,vote])
        sum+=vote
    ranking.sort(key=lambda x:-x[1])

    tmp=sum//2

    if ranking[0][1]==ranking[1][1]:
        print('no winner')
    elif ranking[0][1] <= tmp:
        print('minority winner %d' %(ranking[0][0]))
    else:
        print('majority winner %d' %(ranking[0][0]))