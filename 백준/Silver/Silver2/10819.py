N=int(input())
l=list(map(int,input().split()))
l.sort()
cut=N//2
small_l=[]
for i in range(cut):
  small_l.append(l[i])
  l.remove(l[i])
large_l=l
list=[]

while len(list)!=N:
  list.append(small_l[cut-1])
  list.append()