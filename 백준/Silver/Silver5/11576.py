import sys
input=sys.stdin.readline

A,B=map(int,input().split())
m=int(input())
l=list(map(int,input().split()))
answer=[]
hap=0

for i in range(len(l)):
    m-=1
    hap+=l[i]*(A**m)

while hap!=0:
    answer.append(hap%B)
    hap//=B

answer.reverse()
print(*answer)


