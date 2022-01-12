n=list(map(int,input().split(':')))
m=list(map(int,input().split(':')))

a=m[2]-n[2]
b=m[1]-n[1]
c=m[0]-n[0]

if a<0:
  a+=60
  b-=1
if b<0:
  b+=60
  c-=1
if c<0:
  c+=24
print('%02d:%02d:%02d' %(int(c),int(b),int(a)))


