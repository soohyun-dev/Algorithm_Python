A=int(input())
B=int(input())
C=int(input())
Total=str(A*B*C)
l=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(Total)):
  if Total[i] == '0':
    l[0]+=1
  elif Total[i] == '1':
    l[1]+=1
  elif Total[i] == '2':
    l[2]+=1
  elif Total[i] == '3':
    l[3]+=1
  elif Total[i] == '4':
    l[4]+=1
  elif Total[i] == '5':
    l[5]+=1
  elif Total[i] == '6':
    l[6]+=1
  elif Total[i] == '7':
    l[7]+=1
  elif Total[i] == '8':
    l[8]+=1
  elif Total[i] == '9':
    l[9]+=1
for j in range(10):
  print(l[j])
