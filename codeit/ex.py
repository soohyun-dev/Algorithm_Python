def fn(ar):
  apb=[]
  if len(ar)==1:
    return 1

  for i in range(1, len(ar)):
    if ar[i] != ar[i-1]:
      if ar[i] in apb:
        return 0
      else:
        apb.append(ar[i-1])
  print(apb)
  return 1

n=int(input())
ar=[]
for i in range(n):
  ar.append(input())
cnt=0

for i in range(n):
  cnt+=fn(ar[i])
print(cnt)