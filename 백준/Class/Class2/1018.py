N,M=map(int,input().split())
chess=list()
for i in range(N):
  chess.append(input())
repair=list()

for i in range(N-7):
  for j in range(M-7):
    chess_W=0
    chess_B=0
    for k in range(i,i+8):
      for l in range(j,j+8):
        if  (k+l)%2==0:
          if chess[k][l]!='W':
            chess_W+=1
          if chess[k][l]!='B':
            chess_B+=1
        else: 
          if chess[k][l]!='B':
            chess_W+=1
          if chess[k][l]!='W':
            chess_B+=1
    repair.append(chess_W)
    repair.append(chess_B)
print(min(repair))



    
