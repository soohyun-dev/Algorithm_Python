x, y, z = map(int, input().split()) # 세개의 정수값 받기

sum = 0 # 출력을 몇번하는지 횟수 세주는 변수

for i in range(x):
  for j in range(y):
    for k in range(z):
      print(i, j, k)
      sum+=1 # 출력 횟수

print(sum) # 출력 횟수 값 출력

