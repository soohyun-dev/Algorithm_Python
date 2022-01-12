import sys

N,M=map(int,sys.stdin.readline().split())
l=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):  # 리스트를 2열부터 합으로 바꿔준다.
  for j in range(N):
    if j!=0:  # 2열 부터 값을 변경 시켜준다.
      l[i][j]=l[i][j]+l[i][j-1]   # 1열 값을 2열에 더하고, 나온 값을 3열에 더하고
                                  # 계속 계속 더해간다
for j in range(M):
  sum=0
  x1,y1,x2,y2=map(int,sys.stdin.readline().split())
  for k in range(x1-1,x2):
    if y1!=1:         # 구하려는 시작 열이 1열 이상일 경우 
      sum-=l[k][y1-2]  # 시작하는 열 왼쪽까지 나온 합을 빼준다.
    sum+=l[k][y2-1]  # 구하려는 구간 까지의 합을 더해준다.
  print(sum)


 
