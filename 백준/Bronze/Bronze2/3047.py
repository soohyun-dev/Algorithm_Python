a=list(map(int, input().split()))
a.sort()
A=a[0]
B=a[1]
C=a[2]
l=input()
for i in range(3):
  if l[i]=='A':
    print(A, end=' ')
  elif l[i]=='B':
    print(B, end=' ')
  elif l[i]=='C':
    print(C, end=' ')


