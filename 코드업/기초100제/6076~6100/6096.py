d = [list(map(int ,input().split())) for _ in range(1, 20)]  # 19x19 배열 생성
n = int(input())  # 입력받을 좌표 횟수 입력받음

for i in range(n):
  x, y = map(int,input().split())  # 좌표 입력받기
  for j in range(19):
    if (d[x-1][j]==0):  #해당 좌표 열에 해당하는수 뒤집기
      d[x-1][j]=1
    else:
      d[x-1][j]=0
  for j in range(19):   #해당 좌표 행에 해당하는수 뒤집기
    if(d[j][y-1]==0):
      d[j][y-1]=1
    else:
      d[j][y-1]=0

for k in range(19):  # 배열 출력
  for l in range(19):
    print(d[k][l], end=' ')   
  print()  

