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
    check=True
    loop=M
else:
    people.sort(reverse=True)
    check=False
    loop=N

for i in range(loop):
    if check==True:
        cnt=M-i
    else:
        cnt=i+1
    if sum < people[i]*cnt:
        price=people[i]
        sum=people[i]*cnt
            
print(price, sum)

