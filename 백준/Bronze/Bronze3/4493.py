for i in range(int(input())):
  P1=0
  P2=0
  for j in range(int(input())):
    Player1,Player2=map(str, input().split())
    if(Player1==Player2):
      continue
    elif(Player1=='R' and Player2=='S' or Player1=='P' and Player2=='R' or Player1=='S' and Player2=='P'):
      P1+=1
    elif(Player1=='R' and Player2=='P' or Player1=='P' and Player2=='S' or Player1=='S' and Player2=='R'):
      P2+=1
  if(P1<P2):
    print('Player 2')
  elif(P1>P2):
    print('Player 1')
  else:
    print('TIE')

