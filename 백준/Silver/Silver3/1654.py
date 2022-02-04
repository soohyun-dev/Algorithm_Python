import sys
input=sys.stdin.readline

K,N=map(int,input().split())
lan=[]

for i in range(K):
    lan.append(int(input()))

low, high = 1, max(lan)

while low <= high:
    total=0
    cut=(low+high)//2

    for i in lan:
        total+=(i//cut)
    
    if total >= N:
        low=cut+1
    else: 
        high=cut-1
    print(low, high, total)

print(high)



