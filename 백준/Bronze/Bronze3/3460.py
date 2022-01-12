for i in range(int(input())):
  num=format(int(input()),'b')
  for i,v in enumerate(num[::-1]):
    if v=='1':
      print(i,end=' ')




'''
for i in range(int(input())):
  num=int(input())
  a=format(num,'b')
  for i in reversed(range(len(a))):
    if a[i]=='1':
      print(len(a)-i-1, end=' ')
'''
  
 