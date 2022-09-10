import sys
input=sys.stdin.readline

T=int(input())
dist = [list(map(int,input().split())) for _ in range(T)]

dist=sorted(dist,key=lambda x:x[1])
answer=0
for i in range(T):
    answer+=min([abs(dist[x][0]-dist[i][0]) for x in range(T) if x!=i and dist[x][1]==dist[i][1]])
print(answer)