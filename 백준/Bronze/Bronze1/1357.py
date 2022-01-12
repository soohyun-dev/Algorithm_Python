def REV(X):
  X=list(str(X))
  mirror=''
  for i in range(len(X)-1,-1,-1):
    mirror+=str(X[i])
  return int(mirror)


X,Y=map(int,input().split())

print(REV(REV(X)+REV(Y)))