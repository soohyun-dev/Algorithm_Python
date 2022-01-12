while True:
  l=input()
  l=list(l)
  sum=0
  if l==['#']:
    break
  for i in l:
    if i in 'aeiouAEIOU':
      sum+=1
  print(sum)