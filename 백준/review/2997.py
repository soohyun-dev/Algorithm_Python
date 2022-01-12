n = list(map(int,input().split()))
n.sort()
if (n[1]-n[0] == n[2]-n[1]):
  print(n[2]*2 - n[1])
elif(n[1]-n[0] > n[2]-n[1]):
  print(n[1]*2 - n[2])
else:
  print(n[1]*2 - n[0])
