N,T,C,P=map(int, input().split())
if (N%T==0):
   print(((N//T)-1)*C*P)
else:
   print(((N//T))*C*P)


   