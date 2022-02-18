import sys
input = sys.stdin.readline

N=int(input())
rope=[]
result=[]

for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(N):
    result.append(rope[i]*(i+1))

print(max(result))
