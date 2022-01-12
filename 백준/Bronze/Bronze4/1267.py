N = int(input())
Y=[]
M=[]
y=0
m=0
A = list(map(int, input().split()))
for i in range(N):
  if A[i] >= 60:
    Y.append(20+((A[i]//30)-1)*10)
    M.append(((A[i]//60)+1)*15)
  elif A[i]<=59 and A[i]>=30:
    Y.append(50)
    M.append(15)
  else:
    Y.append(30)
    M.append(15)
for j in range(N):
    y+=Y[j]
    m+=M[j]
if (y==m):
  print("Y M %d" %y)
elif(y>m):
  print("M %d" %m)
else:
  print("Y %d" %y)

