S=input()
a='abcdefghijklmnopqrstuvwxyz'

for i in a:
  if i in S:
    print(S.index(i), end=' ')
  else:
    print(-1, end=' ')
  
