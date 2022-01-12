while True:
  num=int(input())
  if num==0:
    break
  a=int(str(num)[::-1])
  if(num==a):
    print('yes')
  else:
    print('no')

    