for i in range(int(input())):
  N,M=map(int,input().split())
  main=list(map(int,input().split()))
  check=[0 for _ in range(N)]
  check[M]=1
  cnt=0
  while True:
    if main[0]==max(main):
      cnt+=1
      if check[0]!=1:
        del main[0]
        del check[0]
      else:
        print(cnt)
        break
    else:
      main.append(main[0])
      check.append(check[0])
      del main[0]
      del check[0]
