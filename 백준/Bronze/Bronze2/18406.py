N=input()
a=int(len(N)/2)
Asum=0
Bsum=0
for i in range(a):
  Asum+=int(N[i])
for j in range(a,len(N),1):
  Bsum+=int(N[j])

if Asum==Bsum:
  print('LUCKY')
else:
  print('READY')

