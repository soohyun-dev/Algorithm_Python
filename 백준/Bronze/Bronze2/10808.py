a=list(range(97,123))
s=input()
for i in a:
  cnt=s.count(chr(i))
  print(cnt, end=' ')