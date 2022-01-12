N=int(input())
for i in range(N):
  a=list(map(str, input().split()))
  num=float(a[0])
  for j in range(1,len(a)):
    if a[j]=='@':
      num=num*3
    elif a[j]=='%':
      num=num+5
    elif a[j]=='#':
      num=num-7
  print("{:.2f}".format(num))