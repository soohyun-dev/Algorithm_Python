k=[]
for i in range(10):
  A=int(input())
  k.append(A%42)
k=set(k)
print(len(k))