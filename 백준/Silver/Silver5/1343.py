N=str(input())
N=N.replace('XXXX', 'AAAA')
N=N.replace('XX','BB')

if 'X' in N:  # 다 바꿔 줬는데도 X가 남아있을 때
  print(-1)
else:
  print(N)

