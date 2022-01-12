for i in range(int(input())):
  l = list(map(int,input().split()))
  el=[]
  sum=0
  for j in range(len(l)):
    if l[j]%2==0:
      sum+=l[j]
      el.append(l[j])
  print(sum, min(el))
      

      