cup = [1,0,0]
change=input()
for i in change:
  if i == 'A':
    cup[0], cup[1] = cup[1], cup[0]
  elif i == 'B':
    cup[1], cup[2] = cup[2], cup[1]
  else:
    cup[0], cup[2] = cup[2], cup[0]
print(cup.index(1)+1)



'''
a=1
b=0
c=0
d=0
N=str(input())
n=len(N)
for i in range(n):
  if(N[i]=='A'):
    d=b
    b=a
    a=d
  elif(N[i]=='B'):
    d=b
    b=c
    c=d
  else:
    d=a
    a=c
    c=d
if a==1:
  print(1)
elif b==1:
  print(2)
else:
  print(3)
'''


