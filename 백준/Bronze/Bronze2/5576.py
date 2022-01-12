W=[]
K=[]
for i in range(20):
  if i<10:
    W.append(int(input()))
  else:
    K.append(int(input()))
W.sort()
K.sort()
print(sum(W[7:]), sum(K[7:]))


