N=int(input())

check = []
day=[]
pay=[]
dp=[]

for i in range(N):
  a,b=map(int,input().split())
  check.append(N-i)
  if a > check[i]:  # 고를 수 없는 날짜는 0으로 초기화
    a=0
    b=0
  day.append(a)
  pay.append(b)
  dp.append(b)

dp.append(0)  # 밑의 for문 범위를 맞춰주기 위해 추가

for i in range(N-1, -1, -1):
    dp[i] = max(dp[i+1], pay[i]+dp[i+day[i]])
print(dp[0])

