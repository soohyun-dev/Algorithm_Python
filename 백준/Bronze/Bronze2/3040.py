l=[]
for i in range(9):
  l.append(int(input()))
for i in range(9):
  for j in range(i+1,9):
    result=sum(l)-l[i]-l[j]
    if result==100:
      for k in range(9):
        if k==i or k==j:
          continue
        else:
          print(l[k])



