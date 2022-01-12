A,B=map(str,input().split())
Asum=0
Bsum=0

for i in range(len(A)):
  Asum+=int(A[i])
for j in range(len(B)):
  Bsum+=int(B[j])
 
print(Asum*Bsum)
