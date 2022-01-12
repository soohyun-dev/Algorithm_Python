num = int(input())

for i in range(1, num+1):
  if (i % 10 == 3):
    print('X', end=' ')
  elif (i % 10 == 6):
    print('X', end=' ')
  elif (i % 10 == 9):
    print('X', end=' ')
  else:
    print(i, end=' ')


'''
for i in range(1, num+1):
  count = 0
  for j in str(i):
    if j == '3' or j == '6' or j == '9':
      count+=1
  if count > 0:
    i = 'X' * count
  print(i, end=' ')
'''