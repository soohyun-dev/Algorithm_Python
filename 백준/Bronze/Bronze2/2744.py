S=list(input())
for i in range(len(S)):
  if S[i].islower()==True:
    S[i]=S[i].upper()
  else:
    S[i]=S[i].lower()
print(''.join(S))


