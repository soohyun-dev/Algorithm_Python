for i in range(int(input())):
  K=int(input())
  a=1
  sum=0
  answer=0
  while sum<=K:
    sum+=a
    a+=1
    if K==sum:
      answer=1
      print(answer)
      break
  if answer==0:
    print(0)