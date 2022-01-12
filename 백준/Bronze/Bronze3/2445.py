cnt=int(input())
for i in range(1,cnt+1):
  print('*'*i + ' '*2*(cnt-i) + '*'*i)
for i in reversed(range(1,cnt)):
  print('*'*i + ' '*2*(cnt-i) + '*'*i)