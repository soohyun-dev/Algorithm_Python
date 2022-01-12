from collections import Counter
N=int(input())
a=[]
c=[]
for i in range(N):
  name=input()
  a.append(name[0])
cnt=0
a.sort()
n=0
b=Counter(a)
for j,k in b.items():    # j 는 문자, k는 개수를 나타냄
  if k>=5:
    c.append(j)
if c==[]:
  print('PREDAJA')
else:
  for k in range(len(c)):
    print(c[k], end='')


'''
for i in range(1,N):
  if a[n]==a[i]:
    cnt+=1
    n+=1
  else:
    if cnt>=5:
      c.append(a[n])
    n+=1
    cnt=0
    '''


'''

while True:
  if a[0]==a[b]:
    cnt+=1
    b+=1
  elif a[0]!=a[b]:
    if cnt>=5:
      c.append(a[0])
      for j in range(b):
        del(a[j])
      b=1
      cnt=0
    else:
      x=a[b]
      for l in range(b):
        del(a[l])
      b=1
      cnt=0
  if a==[x]:
    break
if c==[]:
  print('PREDAJA')
else:
  for k in range(len(c)):
    print(c[k], end='')
'''