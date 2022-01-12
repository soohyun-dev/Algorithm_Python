alpha=input()
alpha=alpha.upper()
alpha=list(alpha)
if len(alpha)==1:
  print(alpha[0])
else:
  alpha.sort()
  start=alpha[0]
  cnt=0
  max=1
  list=[]
  for i in range(1,len(alpha)):
    if start==alpha[i]:
      cnt+=1
    else:
      cnt=0
      start=alpha[i]
    if cnt>max:
      max=cnt
      list=[]
      list.append(alpha[i])
    elif cnt==max:
      list.append(alpha[i])
  if len(list)==1:
    print(list[0])
  else:
    print('?')


