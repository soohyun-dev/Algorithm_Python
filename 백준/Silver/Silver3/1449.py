import sys
input=sys.stdin.readline

N,L=map(int,input().split())
leak=sorted(list(map(int,input().split())))
left=leak[0]-0.5
right=left+L
cnt=1

for i in range(N):
    if left <= leak[i] <= right:
        continue
    else:
        left=leak[i]-0.5
        right=left+L
        cnt+=1

print(cnt)


