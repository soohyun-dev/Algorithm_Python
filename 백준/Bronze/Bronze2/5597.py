a=list(map(int, range(1,31)))
for i in range(28):
  x=int(input())
  if x in a:
    a.remove(x)
for j in range(len(a)):
  print(a[j])


  