N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
sum=0
while True:
  sum+=max(A)*min(B)
  if len(A)==1:
    break
  A.remove(max(A))
  B.remove(min(B))
  
print(sum)

