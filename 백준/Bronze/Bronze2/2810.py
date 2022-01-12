N = int(input())
sit = list(input())
cup = 1
a=0
for i in range(N):
  if sit[i] == 'S':
    cup+=1
  elif sit[i] == 'L' and a==0:
    a=1
  elif sit[i] == 'L' and a==1:
    a=0
    cup+=1
if cup > N:
  cup = N
print(cup)



