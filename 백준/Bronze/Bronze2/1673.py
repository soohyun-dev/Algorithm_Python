while 1:
  try:
    n,k = map(int,input().split())
    chicken=n
    while n>=k:
      chicken+=n//k
      n=(n//k) + (n%k)
    print(chicken)
  except:
    break