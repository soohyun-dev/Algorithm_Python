N=int(input())
a=list(input().split())
v=input()
sum=0
for i in range(N):
  if a[i]==v:
    sum+=1
print(sum) 
