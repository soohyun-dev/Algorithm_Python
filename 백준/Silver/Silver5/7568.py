import sys
N=int(input())
people=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ranking=[]

for i in range(N):
    rank=1
    for B in people:
        if people[i][0]<B[0] and people[i][1]<B[1]:
            rank+=1

    ranking.append(rank)

print(*ranking)

