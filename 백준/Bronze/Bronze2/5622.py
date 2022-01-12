NUM=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
N=list(input())
time=0
for i in range(len(N)):
  for j in NUM:
    if N[i] in j:
      time+=NUM.index(j)+3
print(time)