a, m, d, n = map(int, input().split())  # 1. 시작값, 2. 곱할 값, 3. 더할 값, 4. 항 개수
cnt = 1  # 연산횟수 세줄 카운트 선언
while (cnt<n):
  a=(a*m+d)  # 연산 후 다음항으로 넘어가기
  cnt+=1  # 카운트 올려가기
print(a)


