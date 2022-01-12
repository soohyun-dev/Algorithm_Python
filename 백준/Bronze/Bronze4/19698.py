N,W,H,L=map(int,input().split())
a=W//L
b=H//L
T=a*b
if(L>W and L>H):  #소 한마리당 공간크기가 헛간보다 클경우
  print(0)
else:
  if(T>N):    # 추첨한 소가 배정 가능한 소 숫자보다 적을경우
    print(N)
  else:
    print(T)


