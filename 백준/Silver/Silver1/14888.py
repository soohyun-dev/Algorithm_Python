n=int(input())
l=list(map(int,input().split()))
sign=[]
result=[]
plus,minus,multiply,division=map(int,input().split())
for i in range(plus):
  sign.append('a')
for i in range(minus):
  sign.append('b')
for i in range(multiply):
  sign.append('c')
for i in range(division):
  sign.append('d')

# xCy  조합
x=(plus+minus+multiply+division)
y=n-1
for i in range(x-1,y-1):
  x=x*i
for j in range(y,0):
  y=y*j
cnt=x//y

