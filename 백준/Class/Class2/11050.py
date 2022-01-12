N,K=map(int,input().split())
s=1
a=1
for i in range(K):
  s=s*(N-i)
for j in range(1,K+1):
  a=a*j
print(int(s/a))