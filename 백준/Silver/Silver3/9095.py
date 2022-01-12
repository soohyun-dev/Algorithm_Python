T=int(input())

def check(T):
  if T==1:
    return 1
  elif T==2:
    return 2
  elif T==3:
    return 4
  else:
    return check(T-1)+check(T-2)+check(T-3)

for i in range(T):
  n=int(input())
  print(check(n))

