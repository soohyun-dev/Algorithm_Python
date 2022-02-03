N=int(input())
cnt=2
while N!=1:
  if N%2==0:
    N//=2
    print(cnt)
  else:
    if N%cnt==0:
      N//=cnt
      print(cnt)
    else:
      cnt+=1



      