for i in range(int(input())):
  num=int(input())
  s=1
  print('Pairs for %d:' %num, end=' ')
  for i in range((num-1)//2):
    if i != 0:
      print(',', end=' ')
    print(s, num-s, end='')
    s+=1
  print()