N=int(input())
a,b=1,1
if N>2:
  for i in range(N-2):
    store=b
    b=a+b
    a=store
print(b)

