import sys
input=sys.stdin.readline

N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
l.sort(key=lambda x:(x[1], x[0]))
end=0
cnt=0
for i in range(N):
    if l[i][0]>=end:
        cnt+=1
        end=l[i][1]

print(cnt)