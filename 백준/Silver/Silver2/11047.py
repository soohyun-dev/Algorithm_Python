N,K=map(int,input().split())
l=[]
for i in range(N):
  l.append(int(input()))
total=0
cnt=N-1
while True:
  if K//l[cnt]>=1:
    a=K//l[cnt]
    total+=a
    K=K-a*l[cnt]
  if K==0:
    print(total)
    break
  cnt-=1


