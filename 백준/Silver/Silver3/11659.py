import sys

N,M=map(int,input().split())
l=list(map(int,sys.stdin.readline().split()))
sum=[0]  # 자릿수 맞춰주기
s=0
for i in range(N):  # 누적합 생성
  s+=l[i]
  sum.append(s)

for i in range(M):
  a,b=map(int,sys.stdin.readline().split())
  print(sum[b]-sum[a-1])

