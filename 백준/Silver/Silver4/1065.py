N=int(input())
cnt=0
for i in range(1,N+1):
  a=0
  i=list(str(i))
  if len(i)==1 or len(i)==2:
    cnt+=1
  elif len(i)>2:
    difference=int(i[1])-int(i[0])
    for j in range(0,len(i)-1):
      if int(i[j+1])-int(i[j])!=difference:
        a=1
    if a==0:
      cnt+=1
print(cnt)



