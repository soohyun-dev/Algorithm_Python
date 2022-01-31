# 분할
def devide(N,M,mat):
  if M==1:
    return mat
  elif M==2:
    return mul(N,mat,mat)
  else:
    d=devide(N,M//2,mat)

    if M%2==0:
      return mul(N,d,d)
    else:
      return mul(N, mul(N,d,d), mat)

# 행렬 곱
def mul(N, left_matrix, right_matrix):
  matrix=[[0]*N for _ in range(N)]  # 내부에 선언해야됨, 안그럼 결과값 달라짐
  
  for i in range(N):
    for j in range(N):
      for k in range(N):
        matrix[i][j]+=left_matrix[i][k]*right_matrix[k][j]
      matrix[i][j]%=1000  # 값이 너무 커지는 것을 방지해서 미리미리 연산
  
  return matrix


N,M=map(int,input().split())
l = [list(map(int,input().split())) for _ in range(N)]

result=devide(N,M,l)

for row in result:
  for element in row:
    print(element%1000, end=' ')  # 마지막 출력전에 한번더 1000으로 나눠주기
  print()