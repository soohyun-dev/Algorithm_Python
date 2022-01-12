for i in range(int(input())):
  n=int(input())
  T=0
  sum=0
  for j in range(1,n+1):
    for k in range (1, j+2):
      T+=k     # 삼각수의 합
    sum+=j*T  # 문제에서 주어진 공식에 적용
    T=0   #sum 에 더해준뒤 T는 다시 0으로 초기화. 
  print(sum)

