num=int(input())
A=[1,2,3]  # 컵 숫자 배정
s=0
for i in range(num):
  x, y = map(int, input().split())   # 바꿀 컵 입력받기
  for j in range(3):
    if (int(A[j])==x):  # 바꿀 x 번 숫자에 해당하는 자릿수 a에 저장
      a=j
    if (int(A[j]==y)):  # 바꿀 y번 숫자에 해당하는 자릿수  b에 저장
      b=j
  s=A[a]      #두 자릿수에 해당하는 컵 서로 바꿔주기
  A[a]=A[b]
  A[b]=s   
print(A[0])



