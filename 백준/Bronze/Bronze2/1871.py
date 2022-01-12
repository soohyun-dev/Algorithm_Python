N=int(input())
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(N):
  front,back = map(str,input().split('-'))
  for j in range(3):
    if front[j] in alpha:
      
