for i in range(int(input())):
  l=list(input())
  result=''
  left=0
  right=0
  for i in range(len(l)):
    if l[i]=='(':
      result='open'
      left+=1
    elif l[i]==')' and right>=left:
      result='open'
      break
    elif l[i]==')':
      result='close'
      right+=1
    
  if right==left and result=='close':
    print('YES')
  else:
    print('NO')


    