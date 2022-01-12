N,W,H=map(int,input().split())
for i in range(N):
  n=int(input())
  D= ((W**2)+(H**2))**(1/2)  # 상자 대각선 길이
  if (n<=W or n<=H or n<=D):
    print('DA')
  else:
    print('NE')


