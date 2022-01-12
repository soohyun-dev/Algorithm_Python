start_N=int(input())
end_N=int(input())
p_list=[]

for i in range(start_N,end_N+1):
  prime=True
  if i >1:
    for j in range(2,i):
      if i%j==0:
        prime=False
        break
    if prime==True:
      p_list.append(i)

if len(p_list)==0:
  print(-1)
else:
  print(sum(p_list))
  print(min(p_list))
  


