import sys
input=sys.stdin.readline

N,M=map(int,input().split())
sum=0
people=[]
pirce=0
for i in range(M):
    people.append(int(input()))

if N>=M:
    people.sort()
    for i in range(M):
        cnt=M-i
        if sum < people[i]*cnt:
            price=people[i]
            sum=people[i]*cnt
else:
    people.sort(reverse=True)
    for i in range(N):
        cnt=i+1
        if sum < people[i]*cnt:
            price=people[i]
            sum=people[i]*cnt

print(price, sum)

