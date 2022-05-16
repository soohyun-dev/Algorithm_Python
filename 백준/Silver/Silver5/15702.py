import sys
input=sys.stdin.readline

record=[0]
N,M=map(int,input().split())
score=list(map(int,input().split()))

sum=0
num=101

for i in range(M):
    tmp=list(input().split())
    cnt=0
    for j in range(1,N+1):
        if tmp[j]=='O':
            cnt+=int(score[j-1])  # 총 몇점인지 계산
            
    if sum < cnt:
        sum=cnt
        num=int(tmp[0])
    elif sum == cnt:
        num=min(num,int(tmp[0]))
        
print(num, sum)