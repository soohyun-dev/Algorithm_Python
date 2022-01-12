i = int(input(), 16)

for j in range(1,16):
  print('%X'%i,'*%X'%j,'=%X'%(i*j),sep='')

'''
for j in range(1, 16):
  print('%X*%X=%X' %(i, j, i*j))
  '''


