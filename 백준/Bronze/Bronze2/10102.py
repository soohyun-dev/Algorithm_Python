N=int(input())
a=input()
vote=[]
for i in range(N):
  vote.append(a[i])

AC=vote.count('A')
BC=vote.count('B')

if AC > BC:
  print('A')
elif AC < BC:
  print('B')
else:
  print('Tie')
