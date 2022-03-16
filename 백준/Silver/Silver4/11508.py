import sys
input=sys.stdin.readline

N=int(input())
num=[int(input()) for i in range(N)]
num.sort(reverse=True)
hap=sum(num)
for i in range(2,N,3):
    hap-=num[i]
print(hap)

