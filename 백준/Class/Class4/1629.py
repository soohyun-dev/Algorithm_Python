def DAC(a, b) :
  if b==1:  # 거듭제곱을 할 필요가 없을 때
    return a % C

  temp = DAC(a, b // 2)

  if b % 2 == 0:  # B가 짝수일 때
    return (temp * temp) % C
  else:  # B가 홀수일 때
    return (temp * temp * a) % C

A, B, C = map(int, input().split())

print(DAC(A, B))


