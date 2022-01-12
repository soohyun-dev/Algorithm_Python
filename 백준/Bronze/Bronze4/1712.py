A,B,C = map(int, input().split())
a = 1
if (B<C):
  while (A+(B*a) >= C*a):
    a+=1
  print(a)
else:
  print(-1)