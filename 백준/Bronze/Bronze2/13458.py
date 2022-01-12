N=int(input())
A=list(map(int,input().split()))
B,C=map(int, input().split())
sum=0
for i in range(N):
  m=A[i]-B
  if m>0:
    sum+=1    # <== 총감독관 우선 카운트
    if m%C==0: # 이후 부 감독관 카운트
      sum+=m//C
    else:
      sum+=(m//C)+1
  else:
    sum+=1
print(sum)

