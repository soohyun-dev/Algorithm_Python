bowl=list(input())
h=10
for i in range(1,len(bowl)):
  if bowl[i]==bowl[i-1]:
    h+=5
  else:
    h+=10
print(h)


