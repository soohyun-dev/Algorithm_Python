import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
steel=list(map(int,input().split()))
steel.sort()
front,back=0,N-1
cnt=0

while front<back:
    if steel[front]+steel[back]==M:
        cnt+=1
        front+=1
        back-=1
    elif steel[front]+steel[back]>M:
        back-=1
    elif steel[front]+steel[back]<M:
        front+=1

print(cnt)