import sys
input=sys.stdin.readline

N=int(input())
vote=[]
cnt=0

for i in range(N):
    vote.append(int(input()))

while max(vote)!=vote[0]:
    tmp=vote.index(max(vote))
    vote[tmp]-=1
    cnt+=1
    vote[0]+=1

for j in range(1,N):
    if vote[0]==vote[j]:
        cnt+=1
        break
print(cnt)