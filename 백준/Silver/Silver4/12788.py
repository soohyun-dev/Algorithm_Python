import sys
input=sys.stdin.readline

N=int(input())
M,K=map(int,input().split())
pen=list(map(int, input().split()))
if M*K>sum(pen):
    print('STRESS')
else:
    pen.sort(reverse=True)
    print(pen)
    sum=0
    cnt=0
    while sum<M*K:
        sum+=pen[cnt]
        cnt+=1
print(cnt)