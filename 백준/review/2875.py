N,M,K=map(int,input().split())
result=0
while(N>=2 and M>=1 and N+M-K>=3):
  N-=2
  M-=1
  result+=1
print(result)

