T=int(input())
for i in range(T):
  A,B=map(int,input().split())
  reward=0
  if A==1:
    reward+=500
  elif A<=3:
    reward+=300
  elif A<=6:
    reward+=200
  elif A<=10:
    reward+=50
  elif A<=15:
    reward+=30
  elif A<=21:
    reward+=10
  elif A==0 or A>21:
    continue

  if B==1:
    reward+=512
  elif B<=3:
    reward+=256
  elif B<=7:
    reward+=128
  elif B<=15:
    reward+=64
  elif B<=31:
    reward+=10
  elif B==0 or B>31:
    continue
  print(reward*10000)