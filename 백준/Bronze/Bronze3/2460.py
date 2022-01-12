total=0
max=0
for i in range(10):
  A,B = map(int,input().split())
  total= total-A+B
  if total>max:
    max=total
print(max)

