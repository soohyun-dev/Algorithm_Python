sum=0
for i in range(8):
  table=str(input())
  for j in range(8):
    if i%2==0 and j%2==0:
      if table[j]=='F':
        sum+=1
    elif i%2!=0 and j%2!=0:
      if table[j]=='F':
        sum+=1
print(sum)






