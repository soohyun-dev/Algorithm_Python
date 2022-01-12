K=int(input())
l=[]
for i in range(K):
  N=input()
  if N=='0':
    l.pop()
  else:
    l.append(int(N))
print(sum(l))

