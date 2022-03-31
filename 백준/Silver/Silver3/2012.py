import sys
input = sys.stdin.readline

N=int(input())
expect=[0]
for i in range(N):
    expect.append(int(input()))
cnt=0
expect.sort()

for i in range(1,N+1):
    cnt+=abs(expect[i]-i)

print(cnt)

