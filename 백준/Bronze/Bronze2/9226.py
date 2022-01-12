import sys
vowels = {
  'a','e','i','o','u'
}
while True:
  a=sys.stdin.readline()
  if a[0]=='#':
    break
  while a[0] not in vowels:
    b=a[0]
    del(a[0])
    a.append(b)
  for i in range(len(a)):
    print(a[i],end='')
  print('ay')

    
