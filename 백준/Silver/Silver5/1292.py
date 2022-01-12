A,B=map(int,input().split())
l=[]
for i in range(1,50):
  for j in range(1,i+1):
    l.append(i)
print(sum(l[A-1:B]))


