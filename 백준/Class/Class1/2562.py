A=[]
for i in range(9):
  A.append(int(input()))
a=max(A)
for j in range(9):
  if a==A[j]:
    print(a)
    print(j+1)
    break
