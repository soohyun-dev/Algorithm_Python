N = int(input())
T=[]
for i in range(N):
  a=list(input())
  T.append(a)
sum=0
l=len(T[0])
for j in range(1,N):
  s=0
  for k in range(l):
    if T[0][k] in T[j]:
      s+=1
  if (s == l and (l-1<=len(T[j])<=l+1)):
    sum+=1
  elif (s+1==l and (l-1<=len(T[j])<=l) ):
    sum+=1
print(sum)

    

