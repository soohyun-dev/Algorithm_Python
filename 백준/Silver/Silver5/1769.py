X=list(input())
cnt=0
while len(X) != 1:
  sum=0
  for i in X:
    sum+=int(i)
  X=list(str(sum))
  cnt+=1

X=int(X[0])
if X % 3 == 0:
  print(cnt, 'YES', sep='\n')
else:
  print(cnt, 'NO', sep='\n')