d=[[0 for j in range(20)]for i in range(20)]  # 19x19 배열을 선언과 동시에 갹자리에 0 대입후, d에 저장.
n = int(input())  # 몇개의 돌을 받을 것인지 입력받기.
for i in range(n):  
  x,y = input().split()  # 배열 몇번째 열과 행에 돌을 놓을 것인지 입력 받기.
  d[int(x)][int(y)]=1  # 해당자리에 돌 놓기 (1 대입)

for i in range(1, 20):  # 19x19배열 칸 모두 출력 빈자리는 0, 돌이 놓인자리는 1
  for j in range(1, 20):
    print(d[i][j], end=' ')   
  print()  # 행에 있는 수를 다 출력하였으면 다음 행으로 이동


