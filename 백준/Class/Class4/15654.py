N, M = map(int, input().split())
l = list(map(int,input().split()))
l.sort()
k=[]

def check():
  a=0
  if len(k)==M:
    for i in range(len(k)-1):
      if k[i] > k[i+1]:
        a=1
      if a==0:
        print(' '.join(map(str, k)))
      a=0
      return
  for i in range(N):
    k.append(l[i])
    check()
    k.pop()

check()




