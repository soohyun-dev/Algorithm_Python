N=int(input())
total=1
for i in range(1,N+1):
  total=i*total
l=list(str(total))
cnt=0
for j in range(len(l)-1,-1,-1):
  if l[j]=='0':
    cnt+=1
  elif l[j]!='0':
    break
print(cnt) 


