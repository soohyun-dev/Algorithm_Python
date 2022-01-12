E,S,M=map(int,input().split())
year=1
e,s,m=1,1,1

while not(E==e and S==s and M==m):
  year+=1
  e+=1
  s+=1
  m+=1
  if e>15:
    e=1
  if s>28:
    s=1
  if m>19:
    m=1
print(year)




