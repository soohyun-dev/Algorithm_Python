import sys

while True:
  l=sys.stdin.readline().rstrip("\n")
  if not l:
    break
  a,A,n,b=0,0,0,0
  for i in range(len(l)):
    if l[i] in map(chr,range(65, 91)):
      A+=1
    elif l[i] in map(chr,range(97,123)):
      a+=1
    elif l[i] in map(str, range(0,10)):
      n+=1
    elif l[i]==' ':
      b+=1
  print(a, A, n, b)
  
  