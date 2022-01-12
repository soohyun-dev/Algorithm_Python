num=int(input())
for i in reversed(range(1, num+1)):
  print(' '*(num-i)+'*'*(2*i-1))
for i in range(2,num+1):
  print(' '*(num-i)+'*'*(2*i-1))
