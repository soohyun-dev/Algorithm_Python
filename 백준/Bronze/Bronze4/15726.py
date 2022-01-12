A,B,C = map(int, input().split())
if(A==min(A,B,C)):
  print(int(A/B*C))
elif(B==min(A,B,C)):
  print(int(A/B*C))
elif(C==min(A,B,C)):
  print(int(A*B/C))
  

