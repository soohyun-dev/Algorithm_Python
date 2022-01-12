T=int(input())
for i in range(T):
  H,W,N=map(int,input().split())
  customer=0
  floor=0
  room=0
  while True:
    room+=1
    for j in range(H):
      floor+=1
      customer+=1
      if customer==N:
        break
    if customer==N:
        break
    floor=0
  print(str(floor)+str(room).zfill(2))
      
    
