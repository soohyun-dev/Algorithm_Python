t=input()
l=[]
for i in range(len(t)):
  l.append(t[i:])

l.sort()

for i in range(len(t)):
  print(l[i])

